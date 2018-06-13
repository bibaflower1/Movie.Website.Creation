import fresh_tomatoes
import media

toy_story = media.Movie("One piece",
	"Une série de mangas shonen créé par Eiichiro Oda",
	"https://media.senscritique.com/media/000017643453/source_big/One_Piece_L_Aventure_de_l_ile_de_l_horloge.jpg",
	"https://youtu.be/eyPr7vlOlH8")
#print(toy_story.storyline)
avatar = media.Movie("Naroto","Une série de mangas shonen créé par Masashi Kashimoto",
	"https://i.paigeeworld.com/user-media/1468972800000/578f25f1868a6ac34d9ee34a_578f2c76868a6ac34d9ee41b_320.jpg",
	"https://youtu.be/WY8gXSA082c")
dragon = media.Movie("Dragon Ball","Une série de mangas shonen créé par Akira Toriyama",
	"http://www.kanzenshuu.com/guides/manga/digital_color/db1_01-lg.png?x10874",
	"https://youtu.be/qMDwsalXtCA")
movies = [toy_story, avatar, dragon]
fresh_tomatoes.open_movies_page(movies)
