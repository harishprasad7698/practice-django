from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
class About(View):
    def get(self,request):
        data={
            "id": 1,
            "full_name": "Adi Kesav",
            "title": "Python Developer",
            "bio": "A passionate developer building scalable applications.",
            "dob": "29/08/2002",
            "email": "adikesav@gmail.com",
            "contact": 9876543211,
            "location": "Kakkanad",
            "github_url": "https://github.com/adi-kesav",
            "linkedin_url": "https://linkedin.com/in/adi-kesav"
            }
        return JsonResponse(data)

class EducationView(View):
    def get(self,request):
        data={
            "id": 101,
            "institution": "Luminar",
            "course": "Python Full Stack",
            "university": "ABC University",
            "location": "Cochin",
            "starting_year": "June 2026",
            "ending_year": "January 2027",
            "cgpa": "7.5",
            "description": "Completed Python Full Stack Development."
            }
        return JsonResponse(data)
class ProjectView(View):
    def get(self,request):
        data1={
             "id": 1,
            "title": "DietLense",
            "short_description": "AI-powered food recognition application.",
            "long_description": "An application that analyzes food images and provides nutritional information.",
            "technologies_used": [
                "Python",
                "Django",
                "Google GenAI SDK"
            ],
            "live_url": "https://dietlense.example.com",
            "github_url": "https://github.com/username/dietlense",
            "image_url": "https://example.com/dietlense.jpg",
            "featured": True
            }
        
        data2={
            
            "id": 2,
            "title": "Interview Prep Blog",
            "short_description": "Educational application for programming interviews.",
            "long_description": "A platform for practicing technical interview questionsand reading programming articles.",
            "technologies_used": [
                "Python",
                "Django",
                "JavaScript"
            ],
            "live_url": "https://prep.example.com",
            "github_url": "https://github.com/username/interview-prep",
            "image_url": "https://example.com/interview.jpg",
            "featured": True
 
        }
        return JsonResponse([data1,data2],safe=False)
    
    
class SkillsView(View):
    def get(self,request):
        data =[
            {
                "id": 1,
                "skill_name": "Python",
                "category": "Programming Language",
                "proficiency": "Advanced",
                "years_of_experience": 4
            },
            {
                "id": 2,
                "skill_name": "Django",
                "category": "Backend",
                "proficiency": "Advanced",
                "years_of_experience": 3
            },
        ]
        return JsonResponse(data,safe=False)
    