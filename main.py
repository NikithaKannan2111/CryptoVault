import tkinter as tk
from tkinter import ttk, messagebox
from cryptography.fernet import Fernet, InvalidToken
import base64

# ---------- COLORS ----------
BG = "#0B1120"
CARD = "#151F32"
ACCENT = "#38BDF8"
GREEN = "#34D399"
WHITE = "#F1F5F9"
MUTED = "#94A3B8"
RED = "#FB7185"


class CryptoVault:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoVault | Secure Message Encryption")
        self.root.geometry("900x720")
        self.root.minsize(760, 650)
        self.root.configure(bg=BG)

        self.setup_style()
        self.build_interface()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Vault.TEntry",
            fieldbackground=CARD,
            foreground=WHITE,
            insertcolor=WHITE,
            bordercolor="#334155",
            padding=10
        )

    def build_interface(self):
        # Header
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=30, pady=(24, 12))

        tk.Label(
            header, text="🔐  CryptoVault",
            font=("Segoe UI", 25, "bold"),
            bg=BG, fg=ACCENT
        ).pack(anchor="w")

        tk.Label(
            header,
            text="SECURE TEXT ENCRYPTION  •  FERNET",
            font=("Segoe UI", 9, "bold"),
            bg=BG, fg=MUTED
        ).pack(anchor="w", pady=(5, 0))

        # Encryption key
        key_card = tk.Frame(self.root, bg=CARD)
        key_card.pack(fill="x", padx=30, pady=10)

        tk.Label(
            key_card, text="ENCRYPTION KEY",
            font=("Segoe UI", 10, "bold"),
            bg=CARD, fg=WHITE
        ).pack(anchor="w", padx=16, pady=(14, 6))

        key_row = tk.Frame(key_card, bg=CARD)
        key_row.pack(fill="x", padx=16, pady=(0, 14))

        self.key_entry = ttk.Entry(
            key_row, style="Vault.TEntry"
        )
        self.key_entry.pack(
            side="left", fill="x", expand=True, padx=(0, 8)
        )

        self.button(
            key_row, "Generate Key", self.generate_key, ACCENT
        ).pack(side="left")

        # Input panel
        input_card = tk.Frame(self.root, bg=CARD)
        input_card.pack(fill="both", expand=True, padx=30, pady=10)

        tk.Label(
            input_card, text="MESSAGE / CIPHERTEXT",
            font=("Segoe UI", 10, "bold"),
            bg=CARD, fg=WHITE
        ).pack(anchor="w", padx=16, pady=(14, 8))

        self.input_text = tk.Text(
            input_card, height=5, wrap="word",
            bg=BG, fg=WHITE, insertbackground=WHITE,
            font=("Consolas", 11),
            relief="flat", padx=12, pady=12
        )
        self.input_text.pack(
            fill="both", expand=True, padx=16, pady=(0, 14)
        )

        # Action buttons
        actions = tk.Frame(self.root, bg=BG)
        actions.pack(fill="x", padx=30, pady=8)

        self.button(
            actions, "🔒  Encrypt", self.encrypt, ACCENT
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.button(
            actions, "🔓  Decrypt", self.decrypt, GREEN
        ).pack(side="left", expand=True, fill="x", padx=5)

        self.button(
            actions, "Clear", self.clear, RED
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))

        # Output panel
        output_card = tk.Frame(self.root, bg=CARD)
        output_card.pack(fill="both", expand=True, padx=30, pady=10)

        output_header = tk.Frame(output_card, bg=CARD)
        output_header.pack(fill="x", padx=16, pady=(14, 8))

        tk.Label(
            output_header, text="RESULT",
            font=("Segoe UI", 10, "bold"),
            bg=CARD, fg=WHITE
        ).pack(side="left")

        self.status = tk.Label(
            output_header, text="Ready",
            font=("Segoe UI", 9),
            bg=CARD, fg=MUTED
        )
        self.status.pack(side="right")

        self.output_text = tk.Text(
            output_card, height=5, wrap="word",
            bg=BG, fg=GREEN, insertbackground=WHITE,
            font=("Consolas", 10),
            relief="flat", padx=12, pady=12
        )
        self.output_text.pack(
            fill="both", expand=True, padx=16, pady=(0, 8)
        )

        self.button(
            output_card, "📋  Copy Result",
            self.copy_result, "#334155"
        ).pack(anchor="e", padx=16, pady=(0, 14))

        # Footer
        tk.Label(
            self.root,
            text="Educational project • Authenticated encryption using Fernet",
            font=("Segoe UI", 9),
            bg=BG, fg=MUTED
        ).pack(pady=(4, 16))

    def button(self, parent, text, command, color):
        return tk.Button(
            parent, text=text, command=command,
            bg=color, fg=BG if color != "#334155" else WHITE,
            activebackground=WHITE, activeforeground=BG,
            font=("Segoe UI", 10, "bold"),
            relief="flat", cursor="hand2",
            padx=14, pady=10
        )

    def generate_key(self):
        key = Fernet.generate_key().decode()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key)
        self.status.config(text="New key generated", fg=GREEN)

    def get_cipher(self):
        key = self.key_entry.get().strip()

        if not key:
            raise ValueError("Generate or enter an encryption key first.")

        try:
            return Fernet(key.encode())
        except (ValueError, TypeError):
            raise ValueError("Invalid key. Generate a valid Fernet key.")

    def show_result(self, result, status):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", result)
        self.status.config(text=status, fg=GREEN)

    def encrypt(self):
        message = self.input_text.get("1.0", "end-1c")

        if not message:
            messagebox.showwarning(
                "Missing Message", "Enter a message to encrypt."
            )
            return

        try:
            cipher = self.get_cipher()
            encrypted = cipher.encrypt(message.encode()).decode()
            self.show_result(encrypted, "Encryption successful")
        except (ValueError, UnicodeError) as error:
            messagebox.showerror("Encryption Error", str(error))

    def decrypt(self):
        ciphertext = self.input_text.get("1.0", "end-1c").strip()

        if not ciphertext:
            messagebox.showwarning(
                "Missing Ciphertext", "Enter ciphertext to decrypt."
            )
            return

        try:
            cipher = self.get_cipher()
            decrypted = cipher.decrypt(ciphertext.encode()).decode()
            self.show_result(decrypted, "Decryption successful")
        except InvalidToken:
            messagebox.showerror(
                "Decryption Failed",
                "The key is incorrect or the ciphertext "
                "has been modified."
            )
            self.status.config(text="Authentication failed", fg=RED)
        except (ValueError, UnicodeError):
            messagebox.showerror(
                "Invalid Input",
                "Check the key and ciphertext format."
            )
            self.status.config(text="Invalid input", fg=RED)

    def copy_result(self):
        result = self.output_text.get("1.0", "end-1c")

        if not result:
            messagebox.showinfo("Copy Result", "There is no result to copy.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        self.status.config(text="Result copied", fg=GREEN)

    def clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status.config(text="Ready", fg=MUTED)


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoVault(root)
    root.mainloop()