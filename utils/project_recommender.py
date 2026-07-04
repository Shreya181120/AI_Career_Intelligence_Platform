def recommend_projects(career, level):

    project_database = {

        "Data Analyst": {

            "Beginner": [

                {
                    "title": "Sales Dashboard using Power BI",
                    "difficulty": "Easy",
                    "skills": "Excel, SQL, Power BI"
                },

                {
                    "title": "Netflix Data Analysis",
                    "difficulty": "Easy",
                    "skills": "Python, Pandas"
                }

            ],

            "Intermediate": [

                {
                    "title": "Customer Segmentation",
                    "difficulty": "Medium",
                    "skills": "Python, SQL, Machine Learning"
                },

                {
                    "title": "Business Intelligence Dashboard",
                    "difficulty": "Medium",
                    "skills": "Power BI, SQL"
                }

            ],

            "Advanced": [

                {
                    "title": "Retail Sales Forecasting",
                    "difficulty": "Hard",
                    "skills": "Python, Time Series, ML"
                },

                {
                    "title": "Fraud Analytics Dashboard",
                    "difficulty": "Hard",
                    "skills": "Python, SQL, Power BI"
                }

            ]
        },

        "Data Scientist": {

            "Beginner": [

                {
                    "title": "Iris Flower Classification",
                    "difficulty": "Easy",
                    "skills": "Python, Scikit-Learn"
                },

                {
                    "title": "Titanic Survival Prediction",
                    "difficulty": "Easy",
                    "skills": "Python, Pandas"
                }

            ],

            "Intermediate": [

                {
                    "title": "House Price Prediction",
                    "difficulty": "Medium",
                    "skills": "Regression, Python"
                },

                {
                    "title": "Customer Churn Prediction",
                    "difficulty": "Medium",
                    "skills": "ML, Pandas"
                }

            ],

            "Advanced": [

                {
                    "title": "Credit Card Fraud Detection",
                    "difficulty": "Hard",
                    "skills": "Machine Learning, Python"
                },

                {
                    "title": "Recommendation System",
                    "difficulty": "Hard",
                    "skills": "ML, Deep Learning"
                }

            ]
        },

        "Machine Learning Engineer": {

            "Beginner": [

                {
                    "title": "Spam Email Detection",
                    "difficulty": "Easy",
                    "skills": "Python, NLP"
                },

                {
                    "title": "Movie Recommendation",
                    "difficulty": "Easy",
                    "skills": "Python"
                }

            ],

            "Intermediate": [

                {
                    "title": "Image Classification",
                    "difficulty": "Medium",
                    "skills": "CNN, TensorFlow"
                },

                {
                    "title": "Sentiment Analysis",
                    "difficulty": "Medium",
                    "skills": "NLP"
                }

            ],

            "Advanced": [

                {
                    "title": "Object Detection",
                    "difficulty": "Hard",
                    "skills": "YOLO, OpenCV"
                },

                {
                    "title": "Medical Image Analysis",
                    "difficulty": "Hard",
                    "skills": "Deep Learning"
                }

            ]
        },

        "AI Engineer": {

            "Beginner": [

                {
                    "title": "AI Chatbot",
                    "difficulty": "Easy",
                    "skills": "Python"
                },

                {
                    "title": "Resume Analyzer",
                    "difficulty": "Easy",
                    "skills": "Python, NLP"
                }

            ],

            "Intermediate": [

                {
                    "title": "Career Recommendation System",
                    "difficulty": "Medium",
                    "skills": "ML, Python"
                },

                {
                    "title": "AI Interview Coach",
                    "difficulty": "Medium",
                    "skills": "Python"
                }

            ],

            "Advanced": [

                {
                    "title": "Multi-Agent AI Assistant",
                    "difficulty": "Hard",
                    "skills": "Granite, LangChain"
                },

                {
                    "title": "RAG Question Answering System",
                    "difficulty": "Hard",
                    "skills": "Granite, ChromaDB"
                }

            ]
        }

    }

    return project_database[career][level]