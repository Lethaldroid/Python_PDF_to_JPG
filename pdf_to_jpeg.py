import os
import pypdfium2 as pdfium

files = []
for file in os.listdir('.'):
    #split the file name and get the extension
    extension = os.path.splitext(file)[1]
    if extension == '.pdf':
        files.append(os.path.abspath(file)) 
        
    # Load a pdf document
for filepath in files:
    filename = os.path.basename(filepath)
    filename = os.path.splitext(filename)[0]
    pdf = pdfium.PdfDocument(filepath)
    page_indices = [i for i in range(len(pdf))]
    renderer = pdf.render_to(pdfium.BitmapConv.pil_image, page_indices = page_indices)
    if not os.path.exists(filename):
        #make a directory to store the images with the same name as the pdf file
        os.mkdir(filename)
        #check if the current directory is the temporary directory
    if os.getcwd() != filename:
        #change directory to the newly created directory
        os.chdir(filename)
        
    for image, index in zip(renderer, page_indices):
        #save the image
        image.save("output_%02d.jpg" % index)
        
    #change directory to the parent directory
    os.chdir('..')