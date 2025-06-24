import gradio as gr
from pipeline import pipeline

def interface(dataset, models):
    if not models:
        return "No models selected", "No models selected", None, None, None
    return pipeline(dataset, models)

gr.Interface(
    fn=interface,
    inputs=[
        gr.Dropdown(["Energy", "Stock", "Traffic", "Weather"], label="Select Dataset"),
        gr.CheckboxGroup(["LSTM", "Transformer", "LiquidML", "XGBoost"], label="Select Models")
    ],
    outputs=[
        gr.Text(label="Train RMSE"),
        gr.Text(label="Test RMSE"),
        gr.Plot(label="Train Forecast"),
        gr.Plot(label="Test Forecast"),
        gr.Plot(label="Model RMSE Comparison")
    ],
    title="Caruana Ensemble Forecaster",
    description="Run a greedy Caruana ensemble on time series predictions from base learners"
).launch()