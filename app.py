import streamlit as st
import ollama
from PyPDF2 import PdfReader
import io
import re

def clean_extracted_text(text):
    """Clean and improve extracted text"""
    if not text:
        return text
    
    # Remove excessive whitespace and line breaks
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Multiple newlines to double
    text = re.sub(r' +', ' ', text)  # Multiple spaces to single
    
    # Fix common extraction issues
    text = re.sub(r'(\w)([A-Z])', r'\1 \2', text)  # Add space before capitals
    text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)  # Add space between numbers and letters
    
    return text.strip()

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file with improved handling"""
    try:
        # Reset file pointer
        pdf_file.seek(0)
        pdf_reader = PdfReader(io.BytesIO(pdf_file.read()))
        
        text = ""
        total_pages = len(pdf_reader.pages)
        
        # Show progress for large PDFs
        if total_pages > 3:
            progress_bar = st.progress(0)
        
        for page_num, page in enumerate(pdf_reader.pages):
            try:
                page_text = page.extract_text()
                if page_text.strip():  # Only add non-empty pages
                    cleaned_text = clean_extracted_text(page_text)
                    text += f"=== PAGE {page_num + 1} ===\n"
                    text += cleaned_text + "\n\n"
                else:
                    text += f"=== PAGE {page_num + 1} (No readable text found) ===\n\n"
                    
                # Update progress
                if total_pages > 3:
                    progress_bar.progress((page_num + 1) / total_pages)
                    
            except Exception as page_error:
                text += f"=== PAGE {page_num + 1} (Error: {str(page_error)}) ===\n\n"
                st.warning(f"Could not extract text from page {page_num + 1}")
        
        # Clean up progress bar
        if total_pages > 3:
            progress_bar.empty()
        
        if not text.strip():
            st.error("❌ No text could be extracted from this PDF.")
            st.info("""
            **Possible reasons:**
            - PDF contains scanned images (not text)
            - PDF is password protected
            - PDF uses complex formatting
            
            **Solutions:**
            - Try converting to a text-based PDF
            - Use a different PDF viewer to save as new PDF
            - Ensure text is selectable in the original PDF
            """)
            return None
        
        # Show extraction stats
        word_count = len(text.split())
        st.success(f"✅ Successfully extracted {word_count} words from {total_pages} page(s)")
            
        return text
        
    except Exception as e:
        st.error(f"❌ Error reading PDF: {str(e)}")
        return None

def analyze_resume_with_ollama(resume_text, job_description=""):
    """Analyze resume using Ollama"""
    
    if job_description:
        prompt = f"""
        Analyze this resume against the job description and provide insights:

        RESUME:
        {resume_text}

        JOB DESCRIPTION:
        {job_description}

        Please provide:
        1. Skills Match Analysis (what matches, what's missing)
        2. Experience Relevance 
        3. Resume Strengths
        4. Areas for Improvement
        5. ATS Optimization Tips
        6. Overall Match Score (1-10)

        Format your response clearly with headers.
        """
    else:
        prompt = f"""
        Analyze this resume and provide comprehensive feedback:

        RESUME:
        {resume_text}

        Please provide:
        1. Key Skills Identified
        2. Experience Summary
        3. Resume Strengths
        4. Areas for Improvement
        5. ATS Optimization Tips
        6. Professional Suggestions

        Format your response clearly with headers.
        """
    
    try:
        response = ollama.chat(
            model='llama3.2:1b',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error analyzing resume: {str(e)}\nMake sure Ollama is running and the model is installed."

def main():
    st.set_page_config(
        page_title="AI Resume Analyzer", 
        page_icon="📄", 
        layout="wide"
    )
    
    st.title("🔍 AI Resume Analyzer")
    st.markdown("Upload your resume and get AI-powered insights to improve your job applications!")
    
    # Sidebar for instructions
    with st.sidebar:
        st.header("📋 How to Use")
        st.markdown("""
        1. Upload your resume (PDF)
        2. Optionally add job description
        3. Click 'Analyze Resume'
        4. Get detailed feedback!
        
        **Requirements:**
        - Ollama must be running
        - llama3.2:1b model installed
        """)
        
        st.header("🚀 Features")
        st.markdown("""
        - Skills analysis
        - ATS optimization tips
        - Job match scoring
        - Improvement suggestions
        - Privacy-focused (local AI)
        """)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📤 Upload Resume")
        uploaded_file = st.file_uploader(
            "Choose your resume (PDF)", 
            type="pdf",
            help="Upload a PDF version of your resume"
        )
        
        st.header("📝 Job Description (Optional)")
        job_description = st.text_area(
            "Paste the job description here for targeted analysis:",
            height=200,
            placeholder="Paste the job posting description here to get specific feedback on how well your resume matches..."
        )
    
    with col2:
        st.header("🤖 AI Analysis")
        
        if uploaded_file is not None:
            # Extract text from PDF
            with st.spinner("Extracting text from resume..."):
                resume_text = extract_text_from_pdf(uploaded_file)
            
            if resume_text:
                # Show extracted text with better formatting
                with st.expander("📄 Extracted Resume Text (Click to expand)"):
                    st.text_area(
                        "Resume Content:", 
                        resume_text[:2000] + "..." if len(resume_text) > 2000 else resume_text, 
                        height=300,
                        help="First 2000 characters shown. Full text is used for analysis."
                    )
                
                # Analyze button
                if st.button("🔍 Analyze Resume", type="primary"):
                    with st.spinner("Analyzing your resume with AI... This may take a moment."):
                        analysis = analyze_resume_with_ollama(resume_text, job_description)
                    
                    st.success("Analysis Complete!")
                    
                    # Display analysis in a nice format
                    st.markdown("## 📊 Resume Analysis Results")
                    st.markdown(analysis)
                    
                    # Download button for analysis
                    st.download_button(
                        label="💾 Download Analysis",
                        data=analysis,
                        file_name="resume_analysis.txt",
                        mime="text/plain"
                    )
        else:
            st.info("👆 Please upload a PDF resume to get started!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "🔒 **Privacy Note**: This tool runs locally using Ollama. "
        "Your resume data stays on your computer and is not sent to external servers."
    )

if __name__ == "__main__":
    main()