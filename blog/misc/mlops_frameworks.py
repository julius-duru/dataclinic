import streamlit as st
import pandas as pd

TITLE = "Choice of ML Frameworks & Vendors for Projects"
CATEGORY = "misc"
KEYWORDS = [
    "machine learning frameworks", "TensorFlow", "PyTorch", "JAX", "scikit-learn",
    "AutoML", "LLM serving", "vLLM", "MLOps", "model deployment", "ONNX",
    "performance benchmarks", "framework selection", "XGBoost", "Hugging Face"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Intermediate → Advanced (Production ML)")
    st.markdown("---")

    # INTRO – conversational tone
    st.write(
        """
        Picking an ML framework can feel overwhelming – TensorFlow, PyTorch, JAX, XGBoost, vLLM… and that’s just the tip of the iceberg.  
        The right choice shapes your **hiring, infrastructure costs, and long‑term maintainability**. This guide walks you through the major players, their sweet spots, and a practical decision framework.

        **In this guide you’ll learn:**  
        - Which frameworks dominate for research, production, tabular data, and LLMs  
        - Real performance benchmarks (training speed, inference throughput)  
        - How to integrate frameworks with MLOps platforms (MLflow, Kubeflow, SageMaker)  
        - A step‑by‑step decision matrix for your project  
        - A beginner‑friendly checklist for every ML implementation

        > Think of this as your **buyer’s guide** – no hype, just what actually works in 2026.
        """
    )
    st.markdown("---")

    # 1. FRAMEWORK VENDORS & THEIR NICHES
    st.header("Major ML Framework Vendors & Their Focus")
    st.write(
        """
        Each major tech company powers one or more frameworks. Understanding their DNA helps you pick the right tool.
        """
    )
    vendors_df = pd.DataFrame({
        "Vendor": ["Google", "Meta (Facebook)", "Microsoft", "Amazon", "Hugging Face", "NVIDIA", "Databricks", "Open Source"],
        "Primary Framework(s)": ["TensorFlow, JAX, Keras", "PyTorch", "ONNX, ML.NET, LightGBM", "SageMaker, MXNet", "Transformers", "RAPIDS.ai", "Spark MLlib", "scikit-learn"],
        "Best For": ["Production AI, Edge, numerical computing", "Research, rapid prototyping", "Cross‑platform deployment, .NET", "Managed cloud ML", "NLP, LLMs, generative AI", "GPU‑accelerated data processing", "Big data distributed ML", "Classical ML, preprocessing"]
    })
    st.dataframe(vendors_df, use_container_width=True)
    st.markdown("---")

    # 2. KEY FRAMEWORKS – detailed table
    st.header("Framework Deep Dive: Strengths and Trade‑offs")
    st.write(
        """
        Here’s a more detailed breakdown – including when to reach for each framework.
        """
    )
    frameworks_df = pd.DataFrame({
        "Framework": ["TensorFlow", "PyTorch", "scikit-learn", "JAX", "XGBoost / LightGBM", "Hugging Face Transformers", "vLLM", "ONNX"],
        "Primary Use Case": ["Production deep learning, Edge AI", "Research, NLP, computer vision", "Classic ML, tabular data", "High‑perf numerical computing", "Gradient boosting on structured data", "NLP, LLMs, generative AI", "LLM inference serving", "Model interoperability"],
        "Key Strengths": ["Mature serving (TFX, TF Serving)", "Dynamic graphs, Pythonic", "Simple, battle‑tested", "GPU/TPU acceleration, autodiff", "Wins most tabular competitions", "Pretrained model hub, tokenizers", "PagedAttention – 2‑3x throughput", "Run PyTorch models in TensorFlow"],
        "Trade‑offs / When to avoid": ["Steep learning curve, verbose", "Production tooling less mature (catching up)", "Not for deep learning or huge scale", "Smaller ecosystem, ops overhead", "Not for unstructured data", "Heavy for inference alone", "Only LLM serving, not training", "Adds complexity, not always needed"]
    })
    st.dataframe(frameworks_df, use_container_width=True)
    st.markdown("---")

    # 3. USE CASES BY FRAMEWORK – expanders for clarity
    st.header("Use Cases")
    
    with st.expander("Tabular / Structured Data", expanded=False):
        st.write(
            """
            **Go‑to**: XGBoost, LightGBM, scikit-learn, CatBoost.  
            **Why**: Gradient boosting still dominates Kaggle and business forecasting.  
            **Example**: Customer churn, credit risk, sales prediction.  
            **AutoML alternative**: AutoGluon or H2O AutoML for zero‑code ensembling.
            """
        )
    
    with st.expander("Deep Learning Research & Prototyping", expanded=False):
        st.write(
            """
            **Go‑to**: PyTorch + Hugging Face (for NLP/CV).  
            **Why**: Dynamic graphs, intuitive debugging, massive community.  
            **Example**: New model architecture, RL, or any paper reproduction.
            """
        )
    
    with st.expander("Production Deep Learning at Scale", expanded=False):
        st.write(
            """
            **Go‑to**: TensorFlow + TFX + TensorFlow Serving.  
            **Why**: Mature deployment tooling, Kubernetes integration, model versioning.  
            **Example**: Recommendation systems, real‑time fraud detection.
            """
        )
    
    with st.expander(" NLP & Large Language Models (LLMs)", expanded=False):
        st.write(
            """
            **Fine‑tuning**: PyTorch + Hugging Face Transformers.  
            **Serving**: vLLM (high throughput) or NVIDIA NIM (max performance).  
            **Example**: Chatbot, summarization, text classification.  
            *Tip:* Use vLLM for production LLMs – Stripe reduced inference costs by 73% after switching.*
            """
        )
    
    with st.expander("Edge / Mobile AI", expanded=False):
        st.write(
            """
            **Go‑to**: TensorFlow Lite, ONNX Runtime, or Core ML.  
            **Why**: Lightweight, quantized models run on phones and IoT.  
            **Example**: On‑device image recognition, gesture detection.
            """
        )
    
    with st.expander("High‑Performance Numerical Computing", expanded=False):
        st.write(
            """
            **Go‑to**: JAX.  
            **Why**: Just‑in‑time compilation, automatic differentiation, runs on GPUs/TPUs.  
            **Example**: Scientific simulations, advanced meta‑learning, or research where speed matters.
            """
        )
    st.markdown("---")

    # 4. PERFORMANCE BENCHMARKS (training & inference)
    st.header("Performance Benchmarks (Real‑world Numbers)")
    st.write(
        """
        Benchmarks change fast, but here are solid 2026 reference points.
        """
    )
    
    with st.expander("Training Speed (Relative)", expanded=False):
        st.write(
            """
            On common deep learning models (ResNet‑50, LSTM):
            - **PyTorch 2.0 + `torch.compile`** – fastest for most architectures (30‑200% improvement over previous PyTorch)
            - **JAX** – within 10‑15% of PyTorch, excellent for large‑scale TPU training
            - **TensorFlow** – slightly slower than PyTorch on dynamic shapes, but very predictable

            > For **tabular data**, XGBoost trains 10‑100x faster than any neural network.
            """
        )
    
    with st.expander("LLM Inference Throughput (Mistral‑7B on A100‑80GB)", expanded=False):
        throughput_df = pd.DataFrame({
            "Framework": ["vLLM", "NVIDIA NIM (TRT‑LLM)", "Hugging Face (naive)", "Ollama (CPU)"],
            "Throughput (tokens/sec)": ["~2,500", "~3,500", "~300", "~150"],
            "Latency (first token)": ["~50 ms", "~30 ms", "~150 ms", "~200 ms"],
            "Startup Time": ["~15s", "~60‑120s", "~10s", "~5s"]
        })
        st.dataframe(throughput_df, use_container_width=True)
        st.caption("vLLM gives the best price/performance for most production LLM workloads. Use NIM if you need absolute peak throughput and have NVIDIA enterprise support.")
    
    with st.expander("AutoML Performance", expanded=False):
        st.write(
            """
            - **H2O AutoML** – Best balance of speed & accuracy, stacked ensembles, enterprise‑ready.  
            - **AutoGluon** – Highest accuracy on most benchmarks, but higher memory usage.  
            - **TPOT** – Great for transparent pipelines (exportable Python code), slower due to genetic programming.  
            """
        )
    st.markdown("---")

    # 5. INTEGRATIONS & MLOps
    st.header("Integrations: Building End‑to‑End ML Pipelines")
    st.write(
        """
        A framework is only one piece. You also need data processing, experiment tracking, and deployment.
        """
    )
    
    with st.expander("Data Processing Integration", expanded=False):
        st.write(
            """
            - **Apache Spark + SynapseML** – Run distributed training (including LightGBM, deep learning) inside Spark pipelines.  
            - **RAPIDS + cuDF** – GPU‑accelerated pandas‑like operations, works with most frameworks via ONNX.  
            - **Data versioning** – DVC (for files) or Delta Lake (for tables) to reproduce any model.
            """
        )
    
    with st.expander("Experiment Tracking & Model Registry", expanded=False):
        st.write(
            """
            | Tool | Best for |
            |------|----------|
            | **MLflow** | Fast, low‑overhead tracking, works with any framework |
            | **Weights & Biases** | Advanced visualizations, collaboration |
            | **TensorBoard** | TensorFlow native, but can read PyTorch logs |
            | **Kubeflow** | Full pipeline orchestration on Kubernetes |
            """
        )
    
    with st.expander("Cross‑Framework Deployment with ONNX", expanded=False):
        st.code(
            "# Export PyTorch model to ONNX\n"
            "import torch\n"
            "dummy_input = torch.randn(1, 3, 224, 224)\n"
            "torch.onnx.export(model, dummy_input, 'model.onnx')\n"
            "\n"
            "# Then serve with ONNX Runtime (C++/Python) or import into TensorFlow\n"
            "import onnxruntime as ort\n"
            "session = ort.InferenceSession('model.onnx')\n"
            "output = session.run(None, {'input': numpy_input})",
            language="python"
        )
    st.markdown("---")

    # 6. DECISION FRAMEWORK – how to choose
    st.header("Decision Framework: How to Choose Each Component")
    st.write(
        """
        Instead of chasing "the best framework", answer these questions in order.
        """
    )
    
    with st.expander("Step 1 – Project Requirements", expanded=False):
        st.write(
            """
            - **Problem type**: Tabular? NLP? Vision? Time series?  
            - **Data size**: <10GB → scikit‑learn / XGBoost; >1TB → Spark MLlib or distributed TensorFlow/PyTorch.  
            - **Latency**: Real‑time (<100ms) favours optimized serving (vLLM, ONNX Runtime).  
            - **Deployment target**: Cloud, edge, browser (TensorFlow.js), mobile (TFLite).
            """
        )
    
    with st.expander("Step 2 – Team & Talent", expanded=False):
        st.write(
            """
            - What frameworks does your team already know?  
            - Local talent pool: PyTorch appears in ~38% of job posts, TensorFlow ~33%.  
            - Learning curve: Keras (easiest) → PyTorch → TensorFlow → JAX (hardest).  
            > A framework with perfect benchmarks is worthless if you can’t hire for it.
            """
        )
    
    with st.expander("Step 3 – Production Readiness", expanded=False):
        st.write(
            """
            - Does the framework have mature serving? (TensorFlow Serving, TorchServe, vLLM)  
            - Are there pre‑built Docker images and Kubernetes operators?  
            - Can you monitor and version models easily? (MLflow integration, Prometheus metrics)
            """
        )
    
    with st.expander("Step 4 – Decision Matrix (Quick Reference)", expanded=False):
        decision_df = pd.DataFrame({
            "If your priority is...": [
                "Research iteration speed & debugging",
                "Production stability & deployment tooling",
                "High‑performance numerical computing at scale",
                "Rapid baseline for tabular data",
                "Low‑latency LLM inference",
                "Edge / mobile deployment"
            ],
            "Choose...": [
                "PyTorch",
                "TensorFlow + TFX",
                "JAX",
                "AutoGluon or H2O AutoML",
                "vLLM (or NVIDIA NIM for max throughput)",
                "TensorFlow Lite"
            ]
        })
        st.dataframe(decision_df, use_container_width=True)
    
    st.markdown("---")

    # 7. BEGINNER'S CHECKLIST (for any ML project)
    st.header("Your End‑to‑End Checklist for ML Project Implementation")
    st.write(
        """
        Copy this into your project plan. It covers framework choice, integration, and governance.
        """
    )
    checklist = """
    **Before you pick a framework:**  
    - [ ] Have I listed my project’s non‑negotiable constraints (latency, data size, team skills)?  
    - [ ] Have I run a small proof‑of‑concept with 2‑3 candidate frameworks?  

    **Data pipeline & versioning:**  
    - [ ] Can I version my datasets (DVC, Delta Lake)?  
    - [ ] Do I have automated data quality checks (Great Expectations)?  

    **Training & experiment tracking:**  
    - [ ] Am I logging hyperparameters, metrics, and model artifacts (MLflow / W&B)?  
    - [ ] Can I reproduce any model from 3 months ago?  

    **Serving & deployment:**  
    - [ ] Does the framework’s inference server meet my latency/throughput needs?  
    - [ ] Have I benchmarked with realistic load?  
    - [ ] Is the model exportable to ONNX if I need cross‑platform?  

    **LLM‑specific (if applicable):**  
    - [ ] Have I tested vLLM or another optimized serving engine?  
    - [ ] Did I consider quantization (FP8, INT4) to reduce costs?  

    **Long‑term maintainability:**  
    - [ ] Is the framework actively maintained (GitHub commits, releases)?  
    - [ ] Does it have a clear deprecation policy?  
    """
    st.markdown(checklist)
    st.success("If you can answer 'yes' to most, you’re on track for a successful production ML project.")
    st.markdown("---")

    # 8. CONCLUSION & NEXT STEPS
    st.header("Don’t Over‑Optimise Too Early")
    st.write(
        """
        Many teams waste weeks comparing benchmarks that don’t reflect their real workload.  
        **Start simple**: scikit‑learn or XGBoost for tabular, PyTorch for deep learning, vLLM for LLM serving.  
        Only optimise when you have evidence of a bottleneck.

        **Your next actions:**  
        1. Take one of your current ML tasks and write down three non‑negotiable constraints (e.g., “must run on a Raspberry Pi”).  
        2. Build a tiny prototype with the simplest framework that fits.  
        3. Run a quick benchmark with a realistic subset of data – measure training time and inference latency.  

        Frameworks come and go, but understanding your own requirements stays forever. Go build something awesome.
        """
    )
    st.markdown("---")

    # 9. EXTERNAL RESOURCES
    st.header("External Resources to Go Deeper")
    st.markdown(
        """
        **Official docs & benchmarks**  
        - [PyTorch vs TensorFlow (MLCommons)](https://mlcommons.org/benchmarks/training/)  
        - [vLLM documentation](https://docs.vllm.ai/)  
        - [ONNX Runtime](https://onnxruntime.ai/)  

        **MLOps & deployment guides**  
        - [MLflow](https://mlflow.org)  
        - [Kubeflow](https://www.kubeflow.org)  
        - [Amazon SageMaker – framework support](https://aws.amazon.com/sagemaker/)  

        **Community & learning**  
        - [Hugging Face Course – learn Transformers + PyTorch](https://huggingface.co/learn/nlp-course)  
        - [Fast.ai – practical deep learning (PyTorch based)](https://www.fast.ai)  
        - [Kaggle – compare frameworks on real datasets](https://www.kaggle.com)  

        **Books**  
        - “Designing Machine Learning Systems” by Chip Huyen (chapter on framework selection)  
        - “Machine Learning Engineering in Action” by Ben Wilson  
        """
    )
    st.markdown("---")
    st.caption("© 2026 | ML Frameworks & Vendors | Make informed, no‑regret choices for production ML.")