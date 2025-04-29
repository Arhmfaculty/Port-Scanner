# 🔍 Python TCP Port Scanner

A lightweight yet powerful Python-based TCP port scanner that allows users to identify open ports on a given IP address or domain within a specified range. Built as part of a cybersecurity training project, this tool is designed to give developers and students a deeper understanding of how port scanning works behind the scenes — without relying on external tools like Nmap.



## 📌 Features

- ✅ Scan a single IP address or domain
- ✅ Specify a custom port range (e.g., 20–1000)
- ✅ Identify and display open TCP ports
- ✅ Track and display total scan duration
- ✅ Resolves domain names to IP addresses
- ✅ Clean CLI interface with input validation
- ✅ Built entirely with Python standard libraries

---

## 🧠 How It Works

The scanner uses Python’s built-in `socket` module to:
1. Resolve a domain name to its corresponding IP address using `socket.gethostbyname()`.
2. Iterate over each port in the user-defined range.
3. Attempt to establish a TCP connection (`socket.SOCK_STREAM`) with a short timeout.
4. Collect and report open ports based on successful connections.

---

## 🖥️ Installation

No external libraries required. The scanner runs with Python 3.6+.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

### 2. Run the Script
```bash
python3 port_scanner.py
```

---

## 📥 Usage

When you run the script, it prompts for:

1. A **domain name or IP address** to scan.
2. A **starting port number**.
3. An **ending port number**.

Example:
```
Enter IP address or domain to scan: scanme.nmap.org
Enter start port: 20
Enter end port: 100
```

### Sample Output
```
Scanning 45.33.32.156 from port 20 to 100...

Open ports on 45.33.32.156: [22, 80]
Scan completed in 0:00:10.512345
```

---

## ⚙️ Code Overview

### Main Functions:

- `portScanner(ip, start_port, end_port)`  
   Performs the actual scan, collects open ports, and prints results.

- `main()`  
   Handles user input, input validation, and calls the `portScanner()`.

### Technologies Used:
- Python 3
- socket module
- datetime module

---

## 🔐 Security & Ethics Note

This scanner is built **strictly for educational and authorized use only**.  
Running scans on networks or domains without explicit permission is **illegal and unethical**.

---

## 🧠 Learning Goals Behind This Project

- Understand the fundamentals of how port scanning works
- Gain hands-on experience with socket programming
- Develop awareness of basic network communication protocols
- Build a useful CLI tool from scratch without external dependencies

---

## 📁 Project Structure

```
port-scanner/
├── port_scanner.py
└── README.md
```

---

## ✅ Future Improvements

- Add multi-threaded scanning for faster performance
- Output scan results to a log or CSV file
- Add banner grabbing for basic service detection
- Include command-line flags (e.g. `--ip`, `--ports`) using `argparse`

---

## 🙌 Acknowledgment

This project was developed as part of an **ethical hacking internship with Hack Secure**, where I explored practical penetration testing, network security, and tool building from scratch.

---

## 📜 License

Feel free to use, modify, or contribute with proper credit.

---
