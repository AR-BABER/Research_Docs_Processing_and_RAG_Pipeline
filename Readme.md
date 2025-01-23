# My Document Processing & RAG Adventure

## The Story Behind This Project
Hey there! This repo documents my journey into the fascinating world of document processing and RAG (Retrieval-Augmented Generation) pipelines. After diving deep into DeepLearning.AI's courses and spending countless hours testing different approaches, I've gathered some pretty cool insights I'd love to share!

## What I've Been Working On

### Unstructured Library - The Swiss Army Knife of Document Processing
First things first - let me tell you about the Unstructured library. It comes in three flavors:
- Serverless
- API
- Local installation

Pro tip: Go for the API or serverless versions - they're way more powerful! Though I did notice they sometimes struggle with image extraction.

### My Testing Adventures

#### HTML Files - The Good Stuff
Here's what worked like a charm:
- Table detection
- Clean metadata extraction
- Stripped away all the HTML metadata
- Nice, clean JSON output
- Got all the text without breaking a sweat

But nothing's perfect - still couldn't grab those image tags!

#### DOCX Files - A Pleasant Surprise
Working with survey documents was pretty interesting:
- Handled those massive multi-page tables like a pro
- Fun fact from Kai: DOCX is basically XML in disguise, which explains why it's so parser-friendly!

### My RAG Pipeline Thoughts

Here's something cool I discovered - instead of jumping straight into similarity search, why not:
1. Take the user's query
2. Let the LLM work its magic to extract any metadata (like dates)
3. Then do the similarity search with metadata filtering

Pretty neat, right? (**)

#### The Metadata Mystery
I found something interesting in L3 - there's this clever metadata filtering system where:
- Element IDs map to embedded objects as parent IDs
- You can track stuff like chapters (e.g., "Malnutrition" as a title)
- All the subheadings link back to their parent chapters
- Small issue: still figuring out the best way to handle those tiny text chunks in the vector DB

### New Chunking Ideas
Got some fresh ideas about chunking:
- Create chunks for each title and its related elements
- If a chunk's too small, just grab the next title and its elements too
- Basically, let the elements guide the chunking process

### Document Processing Deep Dive

#### Rule-based Processing
Perfect for documents with structured info, but PDFs? That's a whole different ball game...

#### Document Image Analysis
This is where it gets really interesting:
- Document Layout Detection → Object Detection Model → Bounding Boxes → OCR
- The YOLOX model is doing some heavy lifting here!

#### Vision Transformer Magic
- Takes a document image
- Spits out text
- One-step processing
- DONUT model showing some promising results

## What's Next?
I've got some synthetic data creation ideas for evaluating the RAG pipeline. Check out these resources I'm working with:
- [My Reference Colab Notebook](https://colab.research.google.com/drive/1VvOauC46xXeZrhh8nlTyv77yvoroMQjr?usp=sharing)
- [Ragas Docs](https://docs.ragas.io/en/latest/getstarted/evaluation.html)

## File Support
This library handles pretty much everything:
- Text files (.txt, .md)
- Word docs (.docx, .doc, .odt)
- Presentations (.pptx, .ppt)
- Spreadsheets (.xlsx, .csv, .tsv)
- Emails (.eml, .msg)
- RTF (.rtf)
- E-books (.epub)
- Web pages (.html, .xml)
- Images (.png, .jpg, .heic)



## Get in Touch
a.r.b.plato@gmail.com