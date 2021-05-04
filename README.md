<h1 align="center">Picklerick</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/nkosi-tauro/picklerick?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/nkosi-tauro/picklerick?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/nkosi-tauro/picklerick?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/nkosi-tauro/picklerick?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/nkosi-tauro/picklerick?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/nkosi-tauro/picklerick?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/nkosi-tauro/picklerick?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Picklerick 🚀 Under construction...  🚧
</h4> 

<hr> -->

<br>

## :dart: About ##

Pickle Rick is a Django Application that makes use of [Rick And Morty API](https://rickandmortyapi.com/)

## 🏡 Architectural Decisions ##

**No Separate Framework Used (e.g Vue)**  
I decided to make use of just Django as it provided me with the required feature sets needed out of the box.

**Usage of Bootstrap**  
Instead of creating my own custom styles, I made use of the Bootstrap library, this was to lessen the time spent on the UI.



## :rocket: Technologies ##

The following tools were used in this project:

- [Django](https://docs.djangoproject.com/)
- [Docker](https://docs.docker.com/)


## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Docker](https://docs.docker.com/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/nkosi-tauro/picklerick

# Access
$ cd picklerick

#Tests
$ python manage.py test rickmorty

# Docker compose build
$ docker-compose build

# Run the project
$ docker-compose up

# Stop the project
$ docker-compose down

# The server will initialize on  <http://localhost:8000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.


Made with :heart: by <a href="https://github.com/nkosi-tauro" target="_blank">Nkosilathi Tauro</a>

&#xa0;

<a href="#top">Back to top</a>
