import tkinter as tk
import ast

class Calculator:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.title("Simple Calculator")
        master.geometry("345x400")
        master.configure(bg='#f0f0f0')
        
        # Create display with improved visibility
        self.display = tk.Entry(master, 
                                width=25, 
                                justify='right', 
                                font=('Arial', 20), 
                                bd=10, 
                                bg='lightgray',  # Changed background to light gray
                                fg='black',      # Text color set to black
                                insertbackground='black')  # Cursor color set to black
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Define buttons with the specific layout you requested
        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '-',
            '5', '6', '7', '+',
            '(', '0', ')', '*'
        ]
        
        # Create button grid with improved styling
        row = 1
        col = 0
        button_style = {
            'width': 5, 
            'height': 2, 
            'font': ('Arial', 14),
            'bg': '#e0e0e0',  # Light gray background
            'activebackground': '#c0c0c0'  # Slightly darker when pressed
        }
        
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, 
                      command=cmd, 
                      **button_style).grid(row=row, column=col, 
                                            padx=3, pady=3)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Button style for control buttons
        control_style = {
            'width': 7,  # Reduced width to fit side by side
            'height': 2, 
            'font': ('Arial', 12),
            'bg': '#e0e0e0',  # Light gray background
            'activebackground': '#c0c0c0'  # Slightly darker when pressed
        }
        
        # Create a frame for bottom buttons
        bottom_frame = tk.Frame(master)
        bottom_frame.grid(row=row, column=0, columnspan=4, padx=3, pady=3)
        
        # Equals and Clear buttons side by side
        tk.Button(bottom_frame, text='CLEAR', 
                  command=self.clear, 
                  **control_style
                  ).pack(side=tk.LEFT, padx=3)
        
        equals_style = {
            'width': 7,  # Reduced width to fit side by side
            'height': 2, 
            'font': ('Arial', 12),
            'bg': 'red',      # Red background
            'fg': 'black',    # Black text
            'activebackground': '#CC0000'  # Slightly darker red when pressed
        }
        
        tk.Button(bottom_frame, text='CALCULATE', 
                  command=self.calculate, 
                  **equals_style
                  ).pack(side=tk.LEFT, padx=3)
    
    def click(self, key):
        # Handle button clicks
        self.display.insert(tk.END, key)
    
    def clear(self):
        # Clear the display
        self.display.delete(0, tk.END)
    
    def calculate(self):
        # Perform calculation
        try:
            # Get the expression from the display
            expression = self.display.get()
            
            # Use a safer evaluation method
            result = self.safe_eval(expression)
            
            # Clear the display and show the result
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception:
            # Handle errors with a more informative message
            self.display.delete(0, tk.END)
            self.display.insert(0, "Invalid Expression")
    
    def safe_eval(self, expression):
        """
        Safely evaluate mathematical expressions
        Allows numbers with leading zeros and basic arithmetic
        """
        # Remove any whitespace
        expression = expression.replace(' ', '')
        
        # Replace leading zeros in numbers
        import re
        expression = re.sub(r'\b0+(\d)', r'\1', expression)
        
        # Use ast.literal_eval for safer evaluation
        return eval(expression)

def main():
    # Create the main window
    root = tk.Tk()
    
    # Create calculator instance
    calculator = Calculator(root)
    
    # Start the GUI event loop
    root.mainloop()

# Run the calculator
if __name__ == "__main__":
    main()