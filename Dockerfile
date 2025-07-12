# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000   
EXPOSE 8501   

# Run both FastAPI and Streamlit together
CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0"]