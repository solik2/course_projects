import requests
import json
from os import walk

"""
REPLACE THE "KEY = 'YOUR API KEY' "
Where you can find your API key => https://www.virustotal.com/gui/my-apikey
"""
KEY = ''

# Load the API key from a JSON file 
# with open('os_chapter/anti_virus/API_KEY.json') as f:
#     KEY = json.load(f)

def request_scan(file_path):
    """
    Sends a file to VirusTotal for scanning.

    Args:
        file_path (str): The full path of the file to be scanned.

    Returns:
        dict: JSON response from the VirusTotal API containing the scan report.
    """
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': KEY['API_ANTI_VIRUS_KEY']}
    # Prepare the file for upload by extracting its name and opening it in binary mode
    files = {'file': (file_path.split("/")[-1], open(file_path, 'rb'))}
    return requests.post(url, files=files, params=params).json()


def request_report(response):
    """
    Retrieves the report of a previously submitted file from VirusTotal.

    Args:
        response (dict): JSON response from the VirusTotal scan request, containing 'resource' and 'scan_id'.

    Returns:
        dict: JSON response from the VirusTotal API containing the scan report.
    """
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': KEY['API_ANTI_VIRUS_KEY'], 'resource': response['resource'], 'scan_id': response['scan_id']}
    # Make the API request to retrieve the report
    return requests.get(url, params=params).json()
    


def virus_detection_on_path(path):
    """
    Scans files for viruses within the specified path.

    Args:
        path (str): Path to a file or directory.

    Returns:
        list: List of dictionaries containing scan reports for each file.
    """
    report = []
    file_name = path.split("/")[-1]
    
    # Check if the path points to a single file or a directory
    if '.' in file_name:
        # Scan a single file
        scan_response = request_scan(path)
        report_response = request_report(scan_response)
        report.append(arrange_response(report_response, file_name))
    else:
        # Scan all files in the directory
        file_paths = []
        layer = 1
        w = walk(path)
        main_folder = path.split("/")[-1]
        print(f'Folder: {main_folder} is being scanned')

        # Collect all file paths in the directory
        for (dirpath, dirnames, filenames) in w:
            for name in filenames:
                file_paths.append(dirpath + "/" + name)   
            layer += 1

        # Scan each file in the directory
        for file_path in file_paths:
            file_name = file_path.split("/")[-1]
            print("Scanning file: " + file_name)
            scan_response = request_scan(file_path)
            report_response = request_report(scan_response)
            arranged_response = arrange_response(report_response, file_name)
            report.append(arranged_response)
            
        # Print summary of scan results
        print(f"The folder {main_folder} has been scanned and have: ")
        malware_count = sum(1 for item in report if item['code'] == 3)
        sus_count = sum(1 for item in report if item['code'] == 2)
        harmless_count = sum(1 for item in report if item['code'] == 1)

        print(str(malware_count) + ' MALWARE Files')
        print(str(sus_count) + ' Sus Files')
        print(str(harmless_count) + ' Harmless Files')

    return report

def arrange_response(response, file_name):
    """
    Organizes the response from the VirusTotal API and classifies the file status.

    Args:
        response (dict): JSON response from the VirusTotal API containing the scan results.
        file_name (str): The name of the file that was scanned.

    Returns:
        dict: Organized response with status and code indicating the file's safety.
    """
    arranged_response = {'file_name': file_name}
    count_detected = 0
    
    # Count the number of detections in the scan results
    for _, value in response['scans'].items():
        if value['detected']:
            count_detected += 1
    
    # Determine the file status based on the number of detections
    if count_detected > len(response['scans']) / 2:
        arranged_response['status'] = 'THE FILE HAS MALWARE!!! :O'
        arranged_response['code'] = 3
        print(file_name + " => MALWARE File!")
    elif count_detected > len(response['scans']) / 4:
        arranged_response['status'] = 'The file may have malware :/'
        arranged_response['code'] = 2
        print(file_name + " => SUS File")
    elif count_detected == 0:
        arranged_response['status'] = 'The file has no malware :D'
        arranged_response['code'] = 1
        print(file_name + " => Harmless File")
    
    return arranged_response

if __name__ == '__main__':
    ls = virus_detection_on_path('/ur/path/goes/here')
