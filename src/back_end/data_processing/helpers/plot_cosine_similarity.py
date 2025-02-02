# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE
#
#
# def plot_recommendation_vectors(instance, dataset_processed, recommended_items, method='tsne',
#                                 save_path='recommendation_plot.png'):
#     """
#     Plots the instance and recommended items in a 2D space using PCA or t-SNE.
#
#     Parameters:
#     - instance (DataFrame): The instance for which recommendations are made.
#     - dataset_processed (DataFrame): The full dataset after preprocessing.
#     - recommended_items (DataFrame): The recommended items.
#     - method (str): Dimensionality reduction method ('pca' or 'tsne').
#     - save_path (str): Path to save the plot.
#     """
#     print("Generating 2D visualization of recommendation vectors...")
#
#     # Extract numerical feature space for visualization
#     feature_columns = dataset_processed.columns.difference(['url', 'title', 'steam_id'])
#     feature_matrix = dataset_processed[feature_columns].values
#
#     # Reduce dimensionality
#     if method == 'pca':
#         reducer = PCA(n_components=2)
#     elif method == 'tsne':
#         reducer = TSNE(n_components=2, perplexity=30, random_state=42)
#     else:
#         raise ValueError("Invalid method. Choose 'pca' or 'tsne'.")
#
#     transformed_features = reducer.fit_transform(feature_matrix)
#
#     # Convert transformed features into a DataFrame
#     reduced_df = pd.DataFrame(transformed_features, columns=['X', 'Y'], index=dataset_processed.index)
#
#     # Identify the instance and recommended items
#     instance_idx = instance.index[0]
#     recommended_idx = recommended_items.index
#
#     # Plot all dataset points
#     plt.figure(figsize=(10, 7))
#     plt.scatter(reduced_df['X'], reduced_df['Y'], alpha=0.3, label='All Items', color='gray')
#
#     # Highlight recommended items
#     plt.scatter(reduced_df.loc[recommended_idx, 'X'], reduced_df.loc[recommended_idx, 'Y'],
#                 color='blue', edgecolors='black', label='Recommended', s=100)
#
#     # Highlight the queried instance
#     plt.scatter(reduced_df.loc[instance_idx, 'X'], reduced_df.loc[instance_idx, 'Y'],
#                 color='red', edgecolors='black', label='Query Instance', s=150, marker='*')
#
#     # Optional: Add annotations for the recommended games
#     for idx in recommended_idx:
#         title = recommended_items.loc[idx, 'title']
#         plt.annotate(title, (reduced_df.loc[idx, 'X'], reduced_df.loc[idx, 'Y']), fontsize=9, alpha=0.7)
#
#     plt.title(f"2D Projection of Recommendation Vectors ({method.upper()})")
#     plt.xlabel("Component 1")
#     plt.ylabel("Component 2")
#     plt.legend()
#     plt.grid(True)
#
#     # plt.xlim([0, 3000])
#     # plt.ylim([0, 300])
#
#     # Save the plot
#     plt.savefig(save_path, dpi=300)
#     plt.close()
#
#     print(f"Plot saved at {save_path}")
