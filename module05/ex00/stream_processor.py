from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    """
    Abstract Base Class for data processing.
    Defines the interface for all specialized processors.
    """
    
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string"""
        return f"Output: {result}"

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data provided to NumericProcessor")

        try:
            total = sum(data)
            avg = total / len(data) if data else 0
            return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            return f"Error processing numeric data: {e}"

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data provided to TextProcessor")
            
        return f"Processed text: {len(data)} characters, {len(data.split())} words"

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data provided to LogProcessor")
            
        try:
            parts = data.split(":", 1)
            level = parts[0].strip()
            message = parts[1].strip()
            
            # Simple logic to determine alert type based on level
            if "ERROR" in level.upper():
                alert_type = "ALERT"
            else:
                alert_type = "INFO"
                
            return f"[{alert_type}] {level} level detected: {message}"
        except Exception as e:
            return f"Error processing log data: {e}"

def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    # 1. Individual Tests
    
    # Numeric
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    if num_proc.validate(data_num):
        print("Validation: Numeric data verified")
        result = num_proc.process(data_num)
        print(num_proc.format_output(result))
    
    # Text
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    data_text = "Hello Nexus World"
    print(f"Processing data: \"{data_text}\"")
    if text_proc.validate(data_text):
        print("Validation: Text data verified")
        result = text_proc.process(data_text)
        print(text_proc.format_output(result))

    # Log
    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    data_log = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_log}\"")
    if log_proc.validate(data_log):
        print("Validation: Log entry verified")
        result = log_proc.process(data_log)
        print(log_proc.format_output(result))

    # 2. Polymorphic Demo
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    
    processors = [
        (num_proc, [1, 2, 3]),
        (text_proc, "Polymorphism is powerful"),
        (log_proc, "INFO: System ready")
    ]
    
    for i, (proc, data) in enumerate(processors, 1):
        try:
            # Polymorphism in action: calling same methods on different objects
            if proc.validate(data):
                res = proc.process(data)
                # Removing 'Output: ' prefix for the result list to match example strictly
                # The example shows: "Result 1: Processed..."
                # But format_output adds "Output: ". 
                # I'll just print the result directly combined with "Result X: " 
                # OR I can rely on format_output but it adds "Output: ".
                # Let's adjust to match example: "Result 1: Processed 3 numeric values..."
                # So I might not use format_output here or format_output is just the content?
                # The example shows "Output: Processed..." earlier.
                # Here it shows "Result 1: Processed...". 
                # I will print manually to match the prompt exactly.
                print(f"Result {i}: {res}")
        except Exception as e:
            print(f"Error: {e}")

    print("Foundation systems online. Nexus ready for advanced streams.")

if __name__ == "__main__":
    main()
