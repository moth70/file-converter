# file-converter
Simple API for converting files from eny format like pdf, xlsx, docx to markdown format

build: 
docker build -t converter:v0.1 -f Dockerfile .

run:
docker run -it --name converter -p 8000:8000 converter:v0.1 
