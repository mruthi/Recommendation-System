def userbased(input_user,user_similarity,user_predictions,similar_user_count,thres):
    #Convert the user_sim table into DataFrame
    user_sim_table=pd.DataFrame(user_similarity)
    #Find similarity user for 78 using cosine table
    similar_input_user= user_sim_table[input_user].sort_values(ascending=True).head(similar_user_count).index
    #Convert in to list
    similar_user_input=list(similar_input_user) 
    #Using similar_user_input,can select movie id from ratings table
    similar_user_movieid_list=[]
    for sim_user in similar_user_input:
        sim=list(ratings[ratings['user_id']==sim_user]['movie_id'])
        similar_user_movieid_list.append(sim)
    #Converting as a whole list
    import itertools
    similar_user_movieid_single_list=list(itertools.chain.from_iterable(similar_user_movieid_list))
    #Unique movieid from the list
    Unique_movieid_similar_user=set(similar_user_movieid_single_list)
    #Input user watched movie_list
    input_user_watched_movieid=list(ratings[ratings['user_id']==input_user]['movie_id'].values)
    #Create a list which should have recom movieid to the input user
    recom=[]
    for per_id in Unique_movieid_similar_user:
        if(per_id in input_user_watched_movieid):
            pass
        else:
            recom.append(per_id)
    #From recommendation list selecting only hightest rated(predicted) value
    highest_Rated=[]
    user_pred=pd.DataFrame(user_prediction)
    user_pred_Trans=user_pred.T
    input_user_pre=pd.DataFrame(user_pred_Trans[input_user])
    input_user_pred=input_user_pre.T
    for re in recom:
        value=input_user_pred[re].values
        if(value>=thres):
            highest_Rated.append(re)
    i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
    'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
    'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,encoding='latin-1')
    #Creating Movie List based on recom movieid
    movie_title=[]
    for movieid in highest_Rated:
        mov=items[items['movie id']==movieid]['movie title'].values
        movie_title.append(mov)
    #Converting into pure list
    movie_title_list=[]
    for m in movie_title:
        print(m)
        mv=list(m)
        movie_title_list.append(mv)
    #Converting into whole list
    import itertools
    Final_Recommend_movie=list(itertools.chain.from_iterable(movie_title_list))
    print("The common Movie in Recom & User:",list(set(recom)&set(input_user_watched_movieid)))
    return Final_Recommend_movie