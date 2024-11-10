# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a_sales = np.random.randint(200, 500, size=12)  # Generate random sales data for Product A
product_b_sales = np.random.randint(300, 600, size=12)  # Generate random sales data for Product B
product_c_sales = np.random.randint(100, 400, size=12)  # Generate random sales data for Product C

# Initialize the plot
plt.figure(figsize=(10, 6))
plt.plot(months, product_a_sales, marker='o', linestyle='-', color='skyblue', label="Product A")
plt.plot(months, product_b_sales, marker='s', linestyle='--', color='salmon', label="Product B")
plt.plot(months, product_c_sales, marker='^', linestyle=':', color='lightgreen', label="Product C")

# Adding Titles and Labels
plt.title("Monthly Sales for Different Products", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Adding Annotations
best_month_idx = np.argmax(product_a_sales)
plt.annotate(
    f'Peak Sale: {product_a_sales[best_month_idx]}',
    xy=(months[best_month_idx], product_a_sales[best_month_idx]),
    xytext=(best_month_idx, product_a_sales[best_month_idx] + 50),
    arrowprops=dict(facecolor='black', arrowstyle="->"),
    fontsize=10,
    color='darkblue'
)

# Adding grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', title="Products", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()
