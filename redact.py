import re

def redact_specific_ip_addresses(log_content, ip1, ip2):
    # Regular expression to match the two specific IP addresses
    ip_pattern = rf'\b(?:{re.escape(ip1)}|{re.escape(ip2)})\b'
    # Replace the specific IP addresses with "REDACTED"
    redacted_content = re.sub(ip_pattern, 'REDACTED', log_content)
    return redacted_content

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def redact_snort_log(input_file, output_file, ip1, ip2):
    # Read the content of the input file
    log_content = read_file(input_file)
    # Redact the specific IP addresses in the log content
    redacted_content = redact_specific_ip_addresses(log_content, ip1, ip2)
    # Write the redacted contenct to the output file
    write_file(output_file, redacted_content)

# Example usage:
input_file = # Add name of file you wish to redact ex. 'filename.txt'
output_file = # Give new file output a name ex. 'filename_redacted.txt
ip1 = # Add IP address 1
ip2 = # Add IP address 2
redact_snort_log(input_file, output_file, ip1, ip2)