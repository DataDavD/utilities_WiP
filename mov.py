import shutil
import os
import fnmatch
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

class Mov():
    """A simple file utility that moves specified borrower docs to a specified folder. Created by DavD."""

    def __init__(self):
        pass

    def muv(self):
        """File/folder mover."""
        doc = []
        while True:
            print()
            ipt = (input("Please enter the list of doc extensions for the files you wish to move (type stop when finished): "))
            if ipt != "stop":
                doc.append(ipt)
            else:
                break

        print()
        pth = input("Please enter the source file path where file list (.txt doc) is located: ")

        print()
        file_nm = input("Please enter the source file name that contains list of files (.txt doc): ")

        print()
        flg = input("Is the folder path the same folder you want the file folders moved to? (Enter Y or N): ")

        src = []
        while True:
            print()
            sc = input("Please enter where the program should search for original borrower docs (one path at a time; type 'stop' when finished): ")
            if sc != "stop":
                src.append(sc)
            else:
                break


        if flg == 'N':
            print()
            dest2 = input("Please enter source folder you wish to send doc folders to: ")

            y=[]
            path2 = pth + file_nm
            with open(path2) as f:
                df_list = [x.strip() for x in f.readlines()]
            for x in df_list:
                os.makedirs(dest2+x)
                for s in src:
                    if os.path.exists(s+x) == True:
                        lst_x = os.listdir(s+x)
                        for file in lst_x:
                            for d in doc:
                                if fnmatch.fnmatch(file,'*'+d+'*')==True:
                                    shutil.copy(s+x+r'\\'+file, dest2+x)
                                    y.append(d)


            results = {}
            for i in doc:
                results[i] = y.count(i)

        else:
            y=[]
            path2 = pth + file_nm
            with open(path2) as f:
                df_list = [x.strip() for x in f.readlines()]
            for x in df_list:
                os.makedirs(pth+x)
                for s in src:
                    if os.path.exists(s+x) == True:
                        lst_x = os.listdir(s+x)
                        for file in lst_x:
                            for d in doc:
                                if fnmatch.fnmatch(file,'*'+d+'*')==True:
                                    shutil.copy(s+x+r'\\'+file, pth+x)
                                    y.append(d)

            results = {}
            for i in doc:
                results[i] = y.count(i)

        print("Move count by file requested: ", results)


    def wtrmk(self):
        """Watermark PDFs."""
        base = r'\\base_path_needed\\'
        print()

        print()
        yn = input("Do you want to watermark a specific file? (Enter Y or N): ")
        if yn=='Y':
            dest = input("Please enter the file path of file to be watermarked: ")
            file1 = input("Please enter file name (must be pdf, i.e. .pdf): ")


            output = PdfFileWriter()
            iname = dest+file1
            ih = open(iname, 'rb')

            wname = base+'wtrmrk.pdf'
            wh = open(wname, 'rb')

            ipdf = PdfFileReader(ih)
            wpdf = PdfFileReader(wh)
            watermark = wpdf.getPage(0)

            for i in range(ipdf.getNumPages()):
                page = ipdf.getPage(i)
                page.mergePage(watermark)
                output.addPage(page)

            with open(dest+'Wtrmkd_'+file1, 'wb') as f:
                output.write(f)


            ih.close()
            wh.close()

            yn2 = input("Do you want to remove the original and rename the watermarked file? (Enter Y or N): ")
            if yn2 == 'Y':
                os.remove(iname)

                for filename in os.listdir(dest):
                    if filename.startswith('Wtrmkd'):
                        os.rename(dest+filename, dest+filename[7:])


        else:
            doc = []
            while True:
                print()
                ipt = (input("Please enter the list of doc extensions for the files you wish to watermark (type stop when finished): "))
                if ipt != "stop":
                    doc.append(ipt)
                else:
                    break

            print()
            pth = input("Please enter the source file path where file list (text doc) is located: ")

            print()
            file_nm = input("Please enter the source file name that contains list of files (.txt doc): ")

            print()
            flg = input("Is the folder path the same folder where the files to be watermarked are? (Enter Y or N): ")

            if flg == 'N':
                print()
                dest2 = input("Please enter folder path where files earmarked to be watermarked are located: ")
                path2 = pth + file_nm
                with open(path2) as f:
                    df_list = [x.strip() for x in f.readlines()]
                for x in df_list:
                    for file in os.listdir(dest2+x):
                        for d in doc:
                            if fnmatch.fnmatch(file,'*'+d+'.pdf')==True:
                                output = PdfFileWriter()

                                iname = dest2+x+r'\\'+file
                                ih = open(iname, 'rb')

                                wname = base+'wtrmrk.pdf'
                                wh = open(wname, 'rb')

                                ipdf = PdfFileReader(ih)
                                wpdf = PdfFileReader(wh)
                                watermark = wpdf.getPage(0)

                                for i in range(ipdf.getNumPages()):
                                    page = ipdf.getPage(i)
                                    page.mergePage(watermark)
                                    output.addPage(page)

                                with open(dest2+x+r'\\'+'Wtrmkd_'+file, 'wb') as f:
                                    output.write(f)

                                ih.close()
                                wh.close()


                print()
                yn3 = input("Do you want to remove the original and rename the watermarked file? (Enter Y or N): ")
                if yn3=='Y':
                    for x in df_list:
                        for file in os.listdir(dest2+x):
                            for d in doc:
                                if fnmatch.fnmatch(file,'name_wanted''+'*'+x+'*'+d+'*')==True:
                                    os.remove(dest2+x+r'\\'+file)

                        for filename in os.listdir(dest2+x):
                            if filename.startswith('Wtrmkd'):
                                os.rename(dest2+x+r'\\'+filename,
                                          dest2+x+r'\\'+filename[7:])

            else:
                path2 = pth + file_nm
                with open(path2) as f:
                    df_list = [x.strip() for x in f.readlines()]
                for x in df_list:
                    for file in os.listdir(pth+x):
                        for d in doc:
                            if fnmatch.fnmatch(file,'*'+d+'.pdf')==True:
                                output = PdfFileWriter()

                                iname = pth+x+r'\\'+file
                                ih = open(iname, 'rb')

                                wname = base+'wtrmrk.pdf'
                                wh = open(wname, 'rb')

                                ipdf = PdfFileReader(ih)
                                wpdf = PdfFileReader(wh)
                                watermark = wpdf.getPage(0)

                                for i in range(ipdf.getNumPages()):
                                    page = ipdf.getPage(i)
                                    page.mergePage(watermark)
                                    output.addPage(page)

                                with open(pth+x+r'\\'+'Wtrmkd_'+file, 'wb') as f:
                                    output.write(f)

                                ih.close()
                                wh.close()

                print()
                yn4 = input("Do you want to remove the original and rename the watermarked file? (Enter Y or N): ")
                if yn4 == 'Y':
                     for x in df_list:
                        for file in os.listdir(pth+x):
                            for d in doc:
                                if fnmatch.fnmatch(file,'name_wanted'+'*'+x+'*'+d+'*')==True:
                                    os.remove(pth+x+r'\\'+file)

                        for filename in os.listdir(pth+x):
                            if filename.startswith('Wtrmkd'):
                                os.rename(pth+x+r'\\'+filename,
                                          pth+x+r'\\'+filename[7:])
