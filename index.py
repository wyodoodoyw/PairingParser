from PyPDF2 import PdfReader
import re
from FlightLeg import FlightLeg
import Pairing

path = '202404-YYZ-PairingFile.PDF.pdf'
    
# def get_info(path):
#    with open(path, 'rb') as f:
#       pdf = PdfReader(f)
#       info = pdf.metadata
#       number_of_pages = len(pdf.pages)
#       print(info)
#       print(number_of_pages)

def get_pdf_content_lines(path):
    with open(path, 'rb') as f:
        pdf_reader = PdfReader(f)
        for page in pdf_reader.pages: 
            for line in page.extract_text().splitlines():
                yield line

def pre_parse_pdf():
  #creates a list of pairings
  file_as_lines = read_file_lines()
  file_as_pairings = convert_lines_to_pairing(file_as_lines)
  return file_as_pairings


def read_file_lines():
  #convert pdf file to array of strings, one string per line
  file_as_lines = []

  for line in get_pdf_content_lines(r'202404-YYZ-PairingFile.PDF.pdf'):
    file_as_lines.append(line)

  return file_as_lines

def convert_lines_to_pairing(file_as_lines):
  #divide file into pairings, detects "=========" to separate pairings
  file_as_pairings = []
  pairing = []

  for i in range(4, len(file_as_lines)):   

    if "=============" in file_as_lines[i]:
        file_as_pairings.append(pairing)
        pairing = []
    else:
      pairing.append(file_as_lines[i])
  return file_as_pairings

pre_parsed = pre_parse_pdf()
#print(pre_parsed)

#for i in range(0, len(pre_parsed[0])):
#  print('[',i,'] ', pre_parsed[0][i])

#print(pre_parsed[0][0])

def convert():
  for i in range(0, 1):#ln(pre_parsed)):
      flights_done = False
      for j in range(0, len(pre_parsed[i])):
        line = pre_parsed[i][j]
        if j==0:
          pairing_number = (re.findall(r"T\d{4}", line))[0]
          date = re.findall(r"\d\d[A-Z]{3}\s-\s\d\d[A-Z]{3}", line)
          pairing_start_date = date[0][0:5]
          pairing_end_date = date[0][8:13]
          print(pairing_number, pairing_start_date, pairing_end_date)
        
        elif j==1:
          number_pr_req = int(re.findall(r"P\s\d{2}", line)[0][-2:])
          number_fa_req = int(re.findall(r"FA\d{2}", line)[0][-2:])
          number_gj_req = int(re.findall(r"GJ\d{2}", line)[0][-2:])
          number_gy_req = int(re.findall(r"GY\d{2}", line)[0][-2:])
          number_bl_req = int(re.findall(r"BL\d{2}", line)[0][-2:])
          # TODO detect all languages, each position if required for the pairing
          print(number_pr_req, number_fa_req, number_gj_req, number_gy_req, number_bl_req)
        elif (re.search(r'-{17,31}',line)):
          #detects -----------------, indicating all flights in pairing parsed
          flights_done = True
        elif (j > 1 and not flights_done):
          #these lines represt the flight legs in the pairing
          flight_operates = line[0:7]
          aircraft_type = line[9:12]
          leg_number = line[17:20]
          leg_origin = line[22:25]
          leg_time = line[27:30]
          leg_destination = line[32:35]
          leg_arrival_time = line[36:40]
          leg_total_duty = line[43:46]
          print(flight_operates, aircraft_type, leg_number, leg_origin, leg_time, leg_destination, leg_arrival_time, leg_total_duty)         
        
convert()