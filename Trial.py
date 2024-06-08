import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\python group\Streamlit\Streamlit\CarPrice_Assignment.csv")

numerical_features = ['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
                      'enginesize', 'boreratio', 'stroke', 'compressionratio', 'horsepower',
                      'peakrpm', 'citympg', 'highwaympg', 'price']
def main():
    st.title('Numerical Features Distribution')

    bins =value=20

    plot_histograms(df, numerical_features, bins)


def plot_histograms(df, numerical_features, bins):
    fig, axes = plt.subplots(3, 5, figsize=(15, 10))
    axes = axes.flatten()

    for i, feature in enumerate(numerical_features):
        ax = axes[i]
        ax.hist(df[feature], bins=20, alpha=0.7)
        ax.set_title(feature)
        ax.set_xlabel('Value')
        ax.set_ylabel('Density')
        plt.tight_layout()
        
    st.pyplot(plt)

if __name__ == "__main__":
    main()

# Define the list of categorical columns to analyze
categorical_columns = ['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                       'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem']

def main():
    st.title('Categorical Variable Analysis')
    
    # Display count plots
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 9))

    # Loop through each categorical column
    for i, column in enumerate(categorical_columns):
        ax = axes[i//3, i%3]  # Get the current axis
        categories = df[column].value_counts().index
        counts = df[column].value_counts().values
        ax.bar(categories, counts, color='skyblue')
        ax.set_title(f'Count Plot of {column.capitalize()}')
        ax.set_xlabel(column.capitalize())
        ax.set_ylabel('Count')

    # Adjust layout and show plots
    plt.tight_layout()
    st.pyplot(fig)

if __name__ == "__main__":
    main()

# Define the number of top car models to plot
n = 20

# Get the top car models
top_car_models = df['CarName'].value_counts().head(n)

def main():
    st.title('Top Car Models by Frequency')
    
    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_car_models.index, top_car_models.values, color='skyblue')
    ax.set_title(f'Top {n} Car Models by Frequency')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Car Model')
    plt.tight_layout()
    
    # Display the plot using Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()

# Define the list of categorical columns to analyze
categorical_columns = ['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                       'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem']

def main():
    st.title('Categorical Feature vs. Price')
    
    # Create subplots with appropriate gaps and larger figure size
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12), 
                             sharex=False, sharey=False,
                             gridspec_kw={'hspace': 0.5, 'wspace': 0.5})

    # Loop through each categorical column
    for i, feature in enumerate(categorical_columns):
        ax = axes[i//3, i%3]  # Get the current axis
        categories = df[feature].unique()
        category_groups = [df[df[feature]==val]['price'] for val in categories]
        ax.boxplot(category_groups)
        ax.set_xticklabels(categories, rotation=45)
        ax.set_title(f'{feature.capitalize()} vs. Price')
        ax.set_xlabel(feature.capitalize())
        ax.set_ylabel('Price')

    # Adjust layout and show plots
    plt.tight_layout()
    
    # Display the plot using Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()

def main():
    st.title('Correlation Analysis')
    
    # Calculate the correlation matrix
    correlation_matrix = df[numerical_features].corr()

    # Create a heatmap using Matplotlib
    fig, ax = plt.subplots(figsize=(15,12))
    im = ax.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
    cbar = ax.figure.colorbar(im, ax=ax)
    
    # Add annotations
    for i in range(len(numerical_features)):
        for j in range(len(numerical_features)):
            ax.text(i, j, f"{correlation_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black' rotation=45)# Set labels
    ax.set_title('Correlation Heatmap')
    ax.set_xticks(range(len(numerical_features)))
    ax.set_yticks(range(len(numerical_features)))
    ax.set_xticklabels(numerical_features)
    ax.set_yticklabels(numerical_features)
    
    # Adjust spacing around the heatmap
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    
    # Show plot
    plt.tight_layout()
    
    # Display the plot using Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
