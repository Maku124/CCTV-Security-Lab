# CCTV Security Lab

A Python-based educational project for learning basic CCTV and
network security concepts.

## Purpose

This project is designed for authorized security testing and
cybersecurity education.

The scanner checks selected TCP ports commonly associated with
network-connected cameras.

## Features

- IPv4 target validation
- Basic TCP port checking
- Common CCTV-related port detection
- Simple terminal output
- No password guessing
- No authentication bypass
- No unauthorized camera access

## Common Ports

| Port | Service | Typical Use |
|------|---------|-------------|
| 80 | HTTP | Web interface |
| 443 | HTTPS | Secure web interface |
| 554 | RTSP | Video streaming |
| 8080 | HTTP-ALT | Alternative web interface |
| 8443 | HTTPS-ALT | Alternative HTTPS interface |

## Usage

Run the scanner against a system you own or are explicitly
authorized to test:

```bash
python3 cctv_scanner.py 127.0.0.1
