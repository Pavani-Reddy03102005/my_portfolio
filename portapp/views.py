from django.shortcuts import render

def index(request):
    context = {
        'name': 'R. Pavani',
        'email': 'pavanireddy0310@gmail.com',
        'phone': '7995264940',
        'about': 'B.Tech CSE student (2027) skilled in Django, Python, and AI/ML. Built full-stack apps including an AI-powered resume matcher using Claude API.',
        'linkedin': 'https://www.linkedin.com/in/pavani-reddy-3412612a6/',
        'github':   'https://github.com/Pavani-Reddy03102005',
        'leetcode': 'https://leetcode.com/u/pavani_reddy_3/',
        'codechef': 'https://www.codechef.com/users/pavani_reddy_3',
        'skills': [
            'Python', 'Java', 'JavaScript', 'SQL',
            'Django', 'Flask', 'HTML', 'CSS', 'AWS', 'Git',
        ],
        'projects': [
            {
                'title': 'AI-Powered Resume Matcher',
                'stack': 'Django · Claude API · scikit-learn',
                'desc':  'Extracts text from resumes, generates AI summaries, and scores job match using TF-IDF cosine similarity.',
                'github': 'https://github.com/Pavani-Reddy03102005',
            },
            {
                'title': 'Dynamic Student LMS',
                'stack': 'Django · HTML · CSS · JavaScript',
                'desc':  'Learning management system with course creation, enrollment, assignments, and role-based access.',
                'github': 'https://github.com/Pavani-Reddy03102005',
            },
        ],
        'internships': [
            {
                'company': 'AWS Cloud',
                'period':  'Sep – Oct 2025',
                'desc':    'Hands-on labs with EC2, S3, IAM and cloud infrastructure basics.',
            },
            {
                'company': 'Google AI/ML',
                'period':  'Oct – Nov 2024',
                'desc':    'Supervised/unsupervised learning, model training and evaluation.',
            },
            {
                'company': 'Zscaler Zero Trust Security',
                'period':  'Aug – Sep 2023',
                'desc':    'Zero Trust architecture and cloud security principles.',
            },
        ],
        'education': [
            {
                'degree': 'B.Tech CSE',
                'school': 'Mother Theresa Institute of Engineering and Technology',
                'year':   '2027 (Expected)',
                'score':  'CGPA 8.6',
            },
            {
                'degree': 'Intermediate (12th)',
                'school': 'Mother Theresa Junior College',
                'year':   '2023',
                'score':  '91%',
            },
            {
                'degree': 'SSC (10th)',
                'school': 'Ravindra Bharathi School',
                'year':   '2021',
                'score':  '99%',
            },
        ],
    }
    return render(request, 'portapp/index.html', context)