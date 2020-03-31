import os
import PyPDF2

def main():
    '''Concatenate pdfs into one pdf'''

    print("Enter the directory path that you wish to squash pdf's in:")
    os.chdir(input())

    print("number of pdf's to squash?")
    num_docs = int(input())

    # add pdf names to array
    pdf_names = []
    for i in range(num_docs):
        print("name of pdf {}?".format(i+1))
        pdf_names.append(input())

    writer = PyPDF2.PdfFileWriter()

    # concatenate files
    i = 0
    file_names = []
    while i < num_docs:
        open_pdf = open(pdf_names[i], "rb")
        pdf = PyPDF2.PdfFileReader(open_pdf)

        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            writer.addPage(page)

        file_names.append(open_pdf)
        i += 1

    # create new pdf
    print("Enter the new pdf doc name:")
    new_pdf = input()
    new_pdf += ".pdf"

    output_file = open(new_pdf, "wb")
    writer.write(output_file)

    # close files
    output_file.close()
    close_files(file_names)


def close_files(file_names):
    '''close all opened files'''
    for f in file_names:
        f.close()

if __name__ == "__main__":
    main()
