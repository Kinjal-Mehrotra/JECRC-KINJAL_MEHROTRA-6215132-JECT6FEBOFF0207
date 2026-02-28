#Hospital Patient Visit Counter
class Solution:

    def department_patient_count(self, visits):
        dept_count = {}
        ## Write your code here & Don't forget to add return keyword

        for element in visits:
            dept=element["department"]
            if dept in dept_count:
                dept_count[dept]+=1
            else:
                dept_count[dept]=1
            
            max_patients_dept=max(dept_count,key=dept_count.get)

        return dept_count,max_patients_dept
