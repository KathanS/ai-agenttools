"""CSV and data manipulation tools using pandas."""

from typing import Annotated
from semantic_kernel.functions import kernel_function

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False


class CSVTools:
    """Tools for working with CSV files and tabular data."""

    def __init__(self):
        """Initialize CSVTools."""
        if not PANDAS_AVAILABLE:
            print("Warning: pandas not installed. Install with: pip install pandas")

    @kernel_function(
        name="read_csv",
        description="Read a CSV file and return its contents as a string"
    )
    def read_csv(
        self,
        file_path: Annotated[str, "Path to the CSV file"],
        max_rows: Annotated[int, "Maximum number of rows to return"] = 100
    ) -> Annotated[str, "CSV contents or error message"]:
        """Read CSV file and return as formatted string."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            return df.head(max_rows).to_string()
        except Exception as err:
            return f"Error reading CSV: {str(err)}"

    @kernel_function(
        name="get_csv_info",
        description="Get information about a CSV file (columns, row count, data types)"
    )
    def get_csv_info(
        self,
        file_path: Annotated[str, "Path to the CSV file"]
    ) -> Annotated[str, "CSV information or error message"]:
        """Get metadata about a CSV file."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            info = []
            info.append(f"Rows: {len(df)}")
            info.append(f"Columns: {len(df.columns)}")
            info.append(f"\nColumn names: {', '.join(df.columns)}")
            info.append(f"\nData types:\n{df.dtypes.to_string()}")
            return "\n".join(info)
        except Exception as err:
            return f"Error reading CSV info: {str(err)}"

    @kernel_function(
        name="filter_csv",
        description="Filter CSV rows based on a column value"
    )
    def filter_csv(
        self,
        file_path: Annotated[str, "Path to the CSV file"],
        column: Annotated[str, "Column name to filter on"],
        value: Annotated[str, "Value to filter for"],
        output_path: Annotated[str, "Path where filtered CSV will be saved"]
    ) -> Annotated[str, "Success or error message"]:
        """Filter CSV based on column value and save to new file."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            
            if column not in df.columns:
                return f"Error: Column '{column}' not found in CSV"
            
            filtered_df = df[df[column].astype(str) == value]
            filtered_df.to_csv(output_path, index=False)
            
            return f"Filtered {len(filtered_df)} rows to: {output_path}"
        except Exception as err:
            return f"Error filtering CSV: {str(err)}"

    @kernel_function(
        name="sort_csv",
        description="Sort CSV by a specific column"
    )
    def sort_csv(
        self,
        file_path: Annotated[str, "Path to the CSV file"],
        column: Annotated[str, "Column name to sort by"],
        output_path: Annotated[str, "Path where sorted CSV will be saved"],
        ascending: Annotated[bool, "Sort in ascending order"] = True
    ) -> Annotated[str, "Success or error message"]:
        """Sort CSV by column and save to new file."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            
            if column not in df.columns:
                return f"Error: Column '{column}' not found in CSV"
            
            sorted_df = df.sort_values(by=column, ascending=ascending)
            sorted_df.to_csv(output_path, index=False)
            
            return f"CSV sorted by '{column}' and saved to: {output_path}"
        except Exception as err:
            return f"Error sorting CSV: {str(err)}"

    @kernel_function(
        name="get_column_stats",
        description="Get statistical summary of a numeric column in a CSV"
    )
    def get_column_stats(
        self,
        file_path: Annotated[str, "Path to the CSV file"],
        column: Annotated[str, "Column name to analyze"]
    ) -> Annotated[str, "Column statistics or error message"]:
        """Get statistical summary of a column."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            
            if column not in df.columns:
                return f"Error: Column '{column}' not found in CSV"
            
            stats = df[column].describe()
            return f"Statistics for '{column}':\n{stats.to_string()}"
        except Exception as err:
            return f"Error getting column stats: {str(err)}"

    @kernel_function(
        name="merge_csv_files",
        description="Merge multiple CSV files with the same columns"
    )
    def merge_csv_files(
        self,
        output_path: Annotated[str, "Path where merged CSV will be saved"],
        input_paths: Annotated[str, "Comma-separated paths of CSV files to merge"]
    ) -> Annotated[str, "Success or error message"]:
        """Merge multiple CSV files into one."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            paths = [p.strip() for p in input_paths.split(',')]
            dfs = [pd.read_csv(path) for path in paths]
            
            merged_df = pd.concat(dfs, ignore_index=True)
            merged_df.to_csv(output_path, index=False)
            
            return f"Successfully merged {len(paths)} CSV files ({len(merged_df)} total rows) to: {output_path}"
        except Exception as err:
            return f"Error merging CSV files: {str(err)}"

    @kernel_function(
        name="select_csv_columns",
        description="Select specific columns from a CSV and save to new file"
    )
    def select_csv_columns(
        self,
        file_path: Annotated[str, "Path to the CSV file"],
        columns: Annotated[str, "Comma-separated column names to select"],
        output_path: Annotated[str, "Path where filtered CSV will be saved"]
    ) -> Annotated[str, "Success or error message"]:
        """Select specific columns from CSV and save to new file."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            column_list = [c.strip() for c in columns.split(',')]
            
            missing_cols = [c for c in column_list if c not in df.columns]
            if missing_cols:
                return f"Error: Columns not found: {', '.join(missing_cols)}"
            
            selected_df = df[column_list]
            selected_df.to_csv(output_path, index=False)
            
            return f"Selected {len(column_list)} columns and saved to: {output_path}"
        except Exception as err:
            return f"Error selecting columns: {str(err)}"

    @kernel_function(
        name="convert_csv_to_json",
        description="Convert a CSV file to JSON format"
    )
    def convert_csv_to_json(
        self,
        file_path: Annotated[str, "Path to the CSV file"],
        output_path: Annotated[str, "Path where JSON file will be saved"]
    ) -> Annotated[str, "Success or error message"]:
        """Convert CSV to JSON format."""
        if not PANDAS_AVAILABLE:
            return "Error: pandas is not installed"
        
        try:
            df = pd.read_csv(file_path)
            df.to_json(output_path, orient='records', indent=2)
            return f"CSV converted to JSON and saved to: {output_path}"
        except Exception as err:
            return f"Error converting CSV to JSON: {str(err)}"
