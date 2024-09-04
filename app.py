import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_population_distribution(dist_type, mean=0, std_dev=1, mean2=0, std_dev2=1, mean3=0, std_dev3=1, size=10000):
    if dist_type == 'Normal':
        return np.random.normal(mean, std_dev, size)
    elif dist_type == 'Trimodal':
        return np.concatenate([np.random.normal(mean, std_dev, size//3), 
                               np.random.normal(mean2, std_dev2, size//3),
                               np.random.normal(mean3, std_dev3, size//3)])
    elif dist_type == 'Uniform':
        return np.random.uniform(mean - std_dev*np.sqrt(3), mean + std_dev*np.sqrt(3), size)
    else:
        raise ValueError("Unsupported distribution type")

def plot_distributions(dist_type='Normal', mean=0, std_dev=1, mean2=0, std_dev2=1, mean3=0, std_dev3=1, n=30, show_population=True, show_sample=True):
    population = generate_population_distribution(dist_type, mean, std_dev, mean2, std_dev2, mean3, std_dev3)
    sample_means = [np.mean(np.random.choice(population, n, replace=False)) for _ in range(1000)]
    
    plt.figure(figsize=(8, 4))
    
    if show_population:
        plt.hist(population, bins=50, density=True, alpha=0.6, color='red', label=f'Population Distribution: {dist_type}')
    
    if show_sample:
        plt.hist(sample_means, bins=50, density=True, alpha=0.6, color='blue', label=f'Sample Mean Distribution (n={n})')
    
    plt.title('Population and Sample Mean Distributions')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    
    plt.show()


# Streamlit App

st.title("Distribution Analyzer")

dist_type = st.selectbox("Distribution Type", ["Normal", "Trimodal", "Uniform"])

col1, col2, col3 = st.columns(3)

with col1:
    mean = st.slider("Mean 1", -10, 10, 0.1)
    std_dev = st.slider("Std Dev 1", 0.1, 5, 0.1)

if dist_type == "Trimodal":
    with col2:
        mean2 = st.slider("Mean 2", -10, 10, 0.1)
        std_dev2 = st.slider("Std Dev 2", 0.1, 5, 0.1)
    with col3:
        mean3 = st.slider("Mean 3", -10, 10, 0.1)
        std_dev3 = st.slider("Std Dev 3", 0.1, 5, 0.1)
else:
    col2.empty()
    col3.empty()

n = st.slider("Sample Size (n)", 1, 30, 1)

show_population = st.checkbox("Show Population")
show_sample = st.checkbox("Show Sample")

plot_distributions(dist_type, mean, std_dev, mean2, std_dev2, mean3, std_dev3, n, show_population, show_sample)
