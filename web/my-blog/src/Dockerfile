# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Define environment variable
ENV FLAG UNBCTF{a11_ab0ut_3nV1r0nm3nT_v4r14bL3s}

# Run app.py when the container launches
CMD ["python", "app.py"]