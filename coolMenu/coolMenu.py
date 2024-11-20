# Function to print colored gradient
def print_gradient(text, color_start, color_end, step, total_steps):
    # ANSI escape codes for colors
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    # Calculate the intermediate color based on the vertical position
    r_start, g_start, b_start = color_start
    r_end, g_end, b_end = color_end
    
    r = int(r_start + (r_end - r_start) * step / total_steps)
    g = int(g_start + (g_end - g_start) * step / total_steps)
    b = int(b_start + (b_end - b_start) * step / total_steps)
    
    # Apply the color to the entire line
    print(f"{rgb_to_ansi(r, g, b)}{text}\033[0m")

# Function to print colored gradient from left to right
def print_gradient_left_to_right(text, color_start, color_end):
    # ANSI escape codes for colors
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    gradient_steps = len(text)
    
    # Extract RGB components for start and end colors
    r_start, g_start, b_start = color_start
    r_end, g_end, b_end = color_end
    
    for i, char in enumerate(text):
        # Calculate intermediate colors for the gradient from left to right
        r = int(r_start + (r_end - r_start) * i / gradient_steps)
        g = int(g_start + (g_end - g_start) * i / gradient_steps)
        b = int(b_start + (b_end - b_start) * i / gradient_steps)
        
        # Apply the color to the character
        print(f"{rgb_to_ansi(r, g, b)}{char}", end="")
    
    print("\033[0m")  # Reset to default color



# Your ASCII art
ascii_art = """
███████╗███╗   ███╗ █████╗ ██╗██╗         ████████╗ ██████╗ ███╗   ██╗███████╗
██╔════╝████╗ ████║██╔══██╗██║██║         ╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝
█████╗  ██╔████╔██║███████║██║██║            ██║   ██║   ██║██╔██╗ ██║█████╗
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║            ██║   ██║   ██║██║╚██╗██║██╔══╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║            ██║   ██║   ██║██║╚██╗██║██╔══╝
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗       ██║   ╚██████╔╝██║ ╚████║███████╗
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝       ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""

# Total number of lines in the ASCII art
total_lines = len(ascii_art.splitlines())

# Define start and end colors for the gradient (light green to pink)
color_start = (144, 238, 144)  # Light Green RGB
color_end = (255, 182, 193)    # Light Pink RGB
# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Define start and end colors for the gradient (yellow to red)
color_start = (255, 255, 0)  # Yellow RGB
color_end = (255, 0, 0)      # Red RGB


# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

print("PLEASE SELECT ONE OF OUR MENU OPTIONS")
print("1. Emojify your text\n2. Colorify your text\n3. Do BOTH\n4. Get a Synonym for a word\n5. Leave.\n\n\n\n")

# Define start and end colors for the gradient (white to blue)
color_start = (255, 255, 255)  # White RGB
color_end = (0, 0, 255)        # Blue RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

# Define start and end colors for the gradient (light cyan/blue to dark blue)
color_start = (0, 255, 255)  # Light Cyan/Blue RGB
color_end = (0, 0, 139)      # Dark Blue RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

# Define start and end colors for the gradient (lighter cyan/blue to dark blue)
color_start = (173, 216, 230)  # Light Sky Blue RGB (lighter cyan/blue)
color_end = (0, 0, 139)        # Dark Blue RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

# Define start and end colors for the gradient (white to blue)
color_start = (255, 255, 255)  # White RGB
color_end = (0, 0, 255)        # Blue RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

# Define start and end colors for the gradient (white to blue)
color_start = (128, 0, 128)  # Purple RGB
color_end = (255, 165, 0)  # Orange RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)


color_start = (255, 255, 255)  # White RGB
color_end = (255, 20, 147)     # Darker pink RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)


color_start = (48, 0, 48)  # Dark Purple RGB
color_end = (255, 165, 0)  # Orange RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)


color_start = (0, 255, 0)        # Green RGB
color_end = (255, 165, 0)  # Orange RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)


color_start = (0, 255, 0)        # Green RGB
color_end = (161, 22, 197)  # Purple RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)


color_start = (255, 255, 7)        # Green RGB
color_end = (0, 0, 255)  # Purple RGB

# Print the gradient from top to bottom
for step, line in enumerate(ascii_art.splitlines()):
    print_gradient(line, color_start, color_end, step, total_lines)

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)
