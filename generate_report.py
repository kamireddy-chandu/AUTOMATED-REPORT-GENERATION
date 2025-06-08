import csv
from fpdf import FPDF
import statistics

# Read data from CSV
def read_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Score'] = int(row['Score'])  # Convert score to int
            data.append(row)
    return data

# Analyze data
def analyze_data(data):
    scores = [item['Score'] for item in data]
    avg = statistics.mean(scores)
    highest = max(data, key=lambda x: x['Score'])
    lowest = min(data, key=lambda x: x['Score'])
    return avg, highest, lowest

# Generate PDF report
def generate_pdf(data, avg, highest, lowest, filename='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Automated Score Report", ln=True, align='C')
    
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Average Score: {avg:.2f}", ln=True)
    pdf.cell(0, 10, f"Highest Score: {highest['Name']} ({highest['Score']})", ln=True)
    pdf.cell(0, 10, f"Lowest Score: {lowest['Name']} ({lowest['Score']})", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Detailed Scores:", ln=True)
    pdf.set_font("Arial", size=12)
    
    for entry in data:
        pdf.cell(0, 10, f"{entry['Name']}: {entry['Score']}", ln=True)
    
    pdf.output(filename)
    print(f"Report generated: {filename}")

# Run the program
if __name__ == "__main__":
    filename = 'data.csv'
    data = read_data(filename)
    avg, highest, lowest = analyze_data(data)
    generate_pdf(data, avg, highest, lowest)
