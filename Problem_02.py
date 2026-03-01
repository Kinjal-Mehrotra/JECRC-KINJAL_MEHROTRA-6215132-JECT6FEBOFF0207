#Student Marks Performance Tracker

class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        ## Write your code here and don't forget to add return keyword

        for element in students:
            m=element["marks"]
            for sub,sco in m.items():
                if sub in subject_total:
                    subject_total[sub]+=sco
                    subject_count[sub]+=1
                else:
                    subject_total[sub]=sco
                    subject_count[sub]=1
            average={}
            for sub in subject_total:
                average[sub]=subject_total[sub]/subject_count[sub]
            
            highest_subject_average=max(average,key=average.get)

        return average,highest_subject_average
    