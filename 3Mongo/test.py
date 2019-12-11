from pymongo import MongoClient


#docker ps -> chercher le port d'entré du container et le mettre dans le client
client = MongoClient("0.0.0.0:27018")


DOCUMENTS = [
    {
    "firstname" : "Thomas",
    "lastname" : "Shelby",
    "position" : "CEO",
    "gender" : "Male",
    "age" : 35,
    "description" : "Thomas 'Tommy' Michael Shelby M.P. OBE, is the leader of the Birmingham criminal gang Peaky Blinders and the patriarch of the Shelby Family. His experiences during and after the First World War have left him disillusioned and determined to move his family up in the world.",
    "nicknames" : ["Tom", "Tommy", "Thomas"],
    "company" : "Peaky Blinders",
    "episodes" : [1,2,4,5,6]
    }, 
{
    "firstname" : "Arthur",
    "lastname" : "Shelby",
    "position" : "Associate",
    "gender" : "Male",
    "age" : 38,
    "description" : "Arthur Shelby Jr. is the eldest of the Shelby siblings and the tough member of Peaky Blinders, the Deputy Vice President Shelby Company Limited. He's also a member of the ICA.",
    "company" : "Peaky Blinders",
    "episodes" : [1,4,6]

},{
    "firstname" : "John",
    "lastname" : "Shelby",
    "position" : "Associate",
    "gender" : "Male",
    "age" : 30,
    "description" : "John Michael Shelby, also called Johnny or John Boy, was the third of Shelby siblings and a member of the Peaky Blinders.",
    "nicknames" : ["Johnny", "John Boy"],
    "company" : "Peaky Blinders",
    "episodes" : [4,5,6]
},{
    "firstname" : "Ada",
    "lastname" : "Thorne",
    "position" : "HR",
    "gender" : "Female",
    "age" : 28,
    "description" : "Ada Thorne is the fourth and only female of the Shelby sibling. She's the Head of Acquisitions of the Shelby Company Limited.",
    "nicknames" : ["Ada Shelby"],
    "company" : "Peaky Blinders",
    "episodes" : [1,2,6]
},{
    "firstname" : "Michael",
    "lastname" : "Gray",
    "position" : "Accounting",
    "gender" : "Male",
    "age" : 21,
    "description" : "Michael Gray is the son of Polly Shelby, his father is dead, and cousin of the Shelby siblings. He is the Chief Accountant in the Shelby Company Limited.",
    "nicknames" : ["Henry Johnson", "Jobbie Muncher", "Mickey"],
    "company" : "Peaky Blinders",
    "episodes" : [5,6]
},{
    "firstname" : "Polly",
    "lastname" : "Gray",
    "gender" : "Female",
    "age" : 45,
    "position" : "CFO",
    "description" : "Elizabeth Polly Gray (née Shelby) is the matriarch of the Shelby Family, aunt of the Shelby siblings, the treasurer of the Birmingham criminal gang, the Peaky Blinders, a certified accountant and company treasurer of Shelby Company Limited. ",
    "nicknames" : ["Aunt Polly", "Polly Gray", "Elizabeth Gray", "Polly Shelby", "Pol"],
    "company" : "Peaky Blinders",
    "episodes" : [1,2,5,6]
}]

db_series = client.series

collection_peaky = db_series['peaky']

collection_peaky.insert_many(DOCUMENTS)

cursor = collection_peaky.find()

for document in cursor :
    print('-----')
    print(document)

shelby = collection_peaky.find({"lastname": "Shelby"})
print(next(shelby))
