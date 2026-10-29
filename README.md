# 🔐 CryptoVault — Secure Text Encryption & Decryption

## Overview
CryptoVault is a Python desktop application that demonstrates secure text encryption and decryption using Fernet authenticated symmetric encryption. It provides a simple graphical interface for protecting confidential text messages.

## Features
- Secure encryption and decryption of text messages
- Fernet encryption key generation
- Authentication checks to detect modified ciphertext or an incorrect key
- Copy encrypted or decrypted results to the clipboard
- Clear input and output fields
- User-friendly graphical interface built with Tkinter
- Error handling for invalid keys and ciphertext

## Technologies Used
- Python 3.10+
- Tkinter
- Cryptography library (Fernet)

## Installation

1. Install Python 3.10 or later.
2. Open a terminal in the project directory.
3. Install the dependency:

   `python -m pip install -r requirements.txt`

## How to Run

Run the following command:

`python main.py`

1. Click **Generate Key**.
2. Enter a message in the input box.
3. Click **Encrypt** to generate ciphertext.
4. Copy the ciphertext into the input box.
5. Click **Decrypt** using the same key to recover the message.

## Cryptographic Concept
CryptoVault uses symmetric encryption, meaning the same secret key is used for encryption and decryption. Fernet combines encryption with authentication so that modified ciphertext or an incorrect key is rejected.

## Limitations
This is an educational mini-project. The application does not store encrypted messages or manage keys for users. Anyone who loses the encryption key will generally be unable to decrypt their messages.

## Future Enhancements
- Encrypted file support
- Secure key export
- Encryption history with appropriate safeguards
- Improved key management

## Author
Nikitha K

## Disclaimer
This project is intended for educational demonstration and is not a complete enterprise key-management solution."# CryptoVault" 
