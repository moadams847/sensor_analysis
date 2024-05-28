from sensor_analysis import load_and_merge_datasets, resample_and_aggregate, get_summary_statistics
from sensor_analysis import plot_scatter_with_one_to_one_line, plot_line_graph, compute_metrics

def main(file_paths, date_formats, resample_freq='h', aggregation_func='mean'):
    merged_df, null_counts = load_and_merge_datasets(file_paths, date_formats)
    
    if merged_df is not None:
        print("Merged DataFrame:")
        print(merged_df.head(2))
        
        print("\nNull Counts Merged:")
        print(null_counts)
        
        resampled_df, null_count_resampled_df = resample_and_aggregate(merged_df, resample_freq, aggregation_func)
        print("Resampled DataFrame:")
        print(resampled_df.head(2))

        print("\nNull Counts Resampled:")
        print(null_count_resampled_df)
        
        if merged_df is not None:
            print("\nMerged DataFrame:")
            print(merged_df)
            
            summary_stats = get_summary_statistics(merged_df)
            print("\nSummary Statistics:")
            print(summary_stats)
            

            def metrics_graphs(df, columns, x_index, y_index):
                plot_scatter_with_one_to_one_line(df, columns[x_index], columns[y_index])
                plot_line_graph(df, 'DataDate', [columns[x_index], columns[y_index]], [df.columns[x_index], df.columns[y_index]])
                rmse, mae, correlation, r_squared, bias = compute_metrics(df, columns[x_index], columns[y_index])
                print(f"\nRMSE: {rmse}")
                print(f"MAE: {mae}")
                print(f"Correlation: {correlation}")
                print(f"R-squared: {r_squared}")
                print(f"Bias: {bias}")

            merged_df_columns = merged_df.columns
            resampled_df_columns = resampled_df.columns

            if len(resampled_df) >= 2:
                metrics_graphs(resampled_df, resampled_df_columns, 2, 5)
            else:
                print("Not enough columns to plot or calculate metrics.")

if __name__ == "__main__":

    file_paths = [
        'data_ENE00960_R.csv',
        'Teledyne_data_Jan_Feb_2024_and_Teledyne_Oct_Nov_2023.csv',
        'weather_data_Jan_Feb_2024_and_Oct_Nov_2023.csv'
        # Add more csv files as needed

    ]

    date_formats = [
        '%d/%m/%Y %H:%M',  # Date format for the first file
        '%d/%m/%Y %H:%M',  # Date format for the second file
        '%d/%m/%Y %H:%M', # Date format for the third file
        # Add more date formats as needed
    ]
    main(file_paths, date_formats)
