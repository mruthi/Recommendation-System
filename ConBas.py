def user_vector(ratings,movie_vector):
    vector=[]
    for user in range(1,944): # Each user id to create vector
        u1=ratings[ratings['user_id']==user][['movie_id','rating']]  
        u1_list=[]
        for i in u1['movie_id']: # Each user watched movie genre vector
            f=movie_vector[i].values
            u1_list.append(f)
        uu1=pd.DataFrame(u1_list,columns=range(1,19))
        vec=[]
        for j in range(1,19): # Sum up the each genre of the user
            g=sum(uu1[j])
            vec.append(g/len(u1))
        vector.append(vec)
    return vector

def content_based(ratings,content_vectors,userid,thresh):
    u2=ratings[ratings['user_id']==userid]['movie_id'].values
    val=content_vectors[content_vectors[userid]>(content_vectors[userid].max()-thresh)][2]
    recom=[]
    for i in val.index:
        if(i in u2):
            pass
        else:
            recom.append(i)
    return recom