from fetch import Fetch
from movie import Movie


title_art = r"""Sistemas Distribuidos     """
print(title_art+'\n')



def main():
    search_result = True
    movie_list = None
    print("Coloque el nombre de la pelicula \n")
    while search_result:
        movie_name = input(" ")
        print(f'Buscando: "{movie_name}" \n')
        movie = Fetch()
        movie_list = movie.Fetch_data(f"list_movies.json?query_term={movie_name}")
        if movie_list['data']['movie_count'] >= 1:
            search_result = False
        else:
            print("Pelicula no encontrada, busque otra por favor\n")

    handle_movie = Movie(movie_list)
    handle_movie.display_movies()

    while handle_movie.valid_index:
        print(f"Coloque ID de la pelicula que quiere ")
        user_choice = input()
        print(f"2.Descargar")
        stream_choice = input()
        if(int(stream_choice) > 1):
            handle_movie.download = True
        handle_movie.handle_movie_stream(user_choice)


main()
