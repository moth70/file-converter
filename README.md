# file-converter
Simple API for converting files from eny format like pdf, xlsx, docx to markdown format

build: 
docker build -t converter:v0.1 -f Dockerfile .

run:
docker run -it --name converter -p 8000:8000 converter:v0.1 

usage:
curl -s -XPOST -F "file=@./kubevirt/images/fedora/odpis_aktualny_100679_1703251323486.pdf" http://127.0.0.1:8000/upload 
or
curl -s -XPOST -F "file=@./kubevirt/images/fedora/odpis_aktualny_100679_1703251323486.pdf" http://127.0.0.1:8000/upload | jq #json pretty view
