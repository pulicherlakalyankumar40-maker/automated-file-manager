from organizer import organize_files
from report import generate_report
directory = r"C:\Users\KALYANKUMAR\Downloads"
print('scanning and organizing files...')
details = organize_files(directory)
if details:
    print('generating report...')
    generate_report(details)
    print('report generated in reports/file_report.csv')
else:
    print('no files to organize.')