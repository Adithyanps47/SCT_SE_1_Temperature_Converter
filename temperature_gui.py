import customtkinter as ctk

# 1. Configuration & Theme
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class TemperatureConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Temperature Converter | SkillCraft Task 01")
        self.geometry("500x450")
        self.resizable(False, False)

        # Title
        self.title_label = ctk.CTkLabel(
            self, 
            text="Temperature Converter", 
            font=("Roboto Medium", 24)
        )
        self.title_label.pack(pady=20)

        # Input Frame (Grouping input elements)
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10, padx=20, fill="x")

        self.entry_label = ctk.CTkLabel(self.input_frame, text="Enter Temperature:")
        self.entry_label.pack(pady=5)

        self.temp_entry = ctk.CTkEntry(self.input_frame, placeholder_text="e.g. 25.5")
        self.temp_entry.pack(pady=10, padx=10, fill="x")

        # Unit Selection Frame
        self.units_frame = ctk.CTkFrame(self)
        self.units_frame.pack(pady=10, padx=20, fill="x")

        # "From" Unit
        self.from_label = ctk.CTkLabel(self.units_frame, text="From:")
        self.from_label.grid(row=0, column=0, padx=10, pady=5)
        self.unit_from = ctk.CTkOptionMenu(
            self.units_frame, 
            values=["Celsius", "Fahrenheit", "Kelvin"]
        )
        self.unit_from.grid(row=0, column=1, padx=10, pady=5)
        self.unit_from.set("Celsius")

        # "To" Unit
        self.to_label = ctk.CTkLabel(self.units_frame, text="To:")
        self.to_label.grid(row=0, column=2, padx=10, pady=5)
        self.unit_to = ctk.CTkOptionMenu(
            self.units_frame, 
            values=["Celsius", "Fahrenheit", "Kelvin"]
        )
        self.unit_to.grid(row=0, column=3, padx=10, pady=5)
        self.unit_to.set("Fahrenheit")

        # Convert Button
        self.convert_btn = ctk.CTkButton(
            self, 
            text="Convert Temperature", 
            command=self.convert,
            height=40,
            font=("Roboto Medium", 14)
        )
        self.convert_btn.pack(pady=20)

        # Result Display
        self.result_label = ctk.CTkLabel(
            self, 
            text="Result will appear here", 
            font=("Roboto", 18),
            text_color="gray"
        )
        self.result_label.pack(pady=10)

    def convert(self):
        try:
            # Get input and units
            val = float(self.temp_entry.get())
            u_from = self.unit_from.get()
            u_to = self.unit_to.get()

            # Base conversion to Celsius first
            if u_from == "Celsius":
                celsius = val
            elif u_from == "Fahrenheit":
                celsius = (val - 32) * 5/9
            elif u_from == "Kelvin":
                celsius = val - 273.15
            
            # Convert from Celsius to Target
            if u_to == "Celsius":
                result = celsius
                symbol = "°C"
            elif u_to == "Fahrenheit":
                result = (celsius * 9/5) + 32
                symbol = "°F"
            elif u_to == "Kelvin":
                result = celsius + 273.15
                symbol = "K"

            # Update Label
            self.result_label.configure(
                text=f"{result:.2f} {symbol}", 
                text_color="#3B8ED0"  # A nice blue color
            )

        except ValueError:
            self.result_label.configure(
                text="Please enter a valid number!", 
                text_color="#FF5555"  # Red for error
            )

if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.mainloop()