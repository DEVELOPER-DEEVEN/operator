import re

class GuardrailService:
    def __init__(self):
        self.blocked_commands = [
            "rm -rf", "format c:", "del /s", "shutdown", "mkfs"
        ]
        self.pii_patterns = [
            r"\b\d{3}-\d{2}-\d{4}\b", # SSN
            r"\b\d{16}\b", # Credit Card
        ]

    def validate_prompt(self, prompt: str) -> tuple[bool, str]:
        """Checks if the prompt is safe. Returns (is_safe, reason)."""
        for cmd in self.blocked_commands:
            if cmd in prompt.lower():
                return False, f"Blocked command detected: {cmd}"
        return True, ""

    def sanitize_output(self, text: str) -> str:
        """Redacts PII from text."""
        sanitized = text
        for pattern in self.pii_patterns:
            sanitized = re.sub(pattern, "[REDACTED]", sanitized)
        return sanitized

    def check_screen_safety(self, ocr_text: str) -> bool:
        """Checks if screen content is safe to process (e.g. no sensitive data)."""
        # Placeholder for more complex logic
        return True
