import ddf.minim.*;
import processing.video.*;

Minim minim;
AudioPlayer song;
Movie[] habilidadesMovies;

//Lucas - informações dos pokemons
PImage ivysaur, bulbasaur, venusaur, squirtle, wartortle, blastoise, charmander, charmelion, charizard;
PImage[] pokemon = new PImage[9]; // Cria um array com as imagens dos 9 Pokémons
String[] names = {"Bulsaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise"}; // Array de nomes de Pokémon
String[] types = {"Grama e Venenoso", "Grama e Venenoso", "Grama e venenoso", "Fogo", "Fogo", "Fogo e Voador", "Água", "Água", "Água"}; // Array de tipos de Pokémon
String[] altura = {"Altura: 0.7m", "Altura: 1.0m", "Altura: 2.0m", "Altura: 0.6m", "Altura: 1.1m", "Altura: 1.7m", "Altura: 0.5m", "Altura: 1.0m", "Altura: 1.6m"};
String[] peso = {"Peso: 6.9 Kg", "Peso: 13.0 Kg", "Peso: 100.0Kg", "Peso: 8.5 Kg", "Peso: 19.0 Kg", "Peso: 90.5 Kg", "Peso: 9.0 Kg", "Peso: 22.5 Kg", "Peso: 85.5 Kg"};
String[] habilidade1 = {"Razor Leaf", "Vine Whip", "Sleep Powder", "Ember", "Ember", "Ember", "Water Gun", "Water Gun", "Water Gun"};
String[] habilidade2 = {"Vine Whip", "Sleep Powder", "Vine Whip", "Fire Spin", "Dragon Breath", "Dragon Breath", "Hydro Pump", "Water Gun", "Ice Bean"};
int i = 0;
int visivel = 0;

//
PImage imagem_fundo, pokedex, display;
int svar = 1;
int index = 0;
int video = 0;
int movie = 0;
String[] habilidades = { "vine_whip", "razor_leaf","vine_whip","sleep_powder","sleep_powder_venosaur", "vine_whip_venosaur","ember","fire_spin","ember_charmeleon", "dragon_breath","ember_charlizard", "dragon_breath", "water_gun", "hydro_pump", "water_gun_wartortle", "hydro_pump", "water_gun_blastoise", "ice_bean" };


void setup() {
  size(1050, 654);
  textSize(50);
  imagem_fundo = loadImage("background.PNG");
  pokedex = loadImage("pokedex.png");
  background(imagem_fundo);
  size(1050,654);
  textSize(50);
  imagem_fundo = loadImage("background.PNG");
  pokedex = loadImage("pokedex.png");
  
  minim = new Minim(this);
  song = minim.loadFile("anville.mp3");
  song.play();
  song.loop();
  
  habilidadesMovies = new Movie[18];
  for (i=0; i< 18; i++) {
    habilidadesMovies[i] = new Movie(this, habilidades[i] + ".mp4"); // declara um array com o nome dos videos das habilidades de cada pokemon
    
  }

//Lucas - altera o valor do i conforme é adicionado(+i caso clique para a direita)
  for (int i = 0; i < pokemon.length; i++) {
    String filename = "pokemon_" + i + ".JPEG"; // declara o nome do arquivo para buscar, mudando o indice ele troca de imagem
    if (!dataFile(filename).exists()) {
      filename = "pokemon_" + i + ".jpeg";      
    } //caso o nome do arquivo esteja em JPG minúsuculo
    pokemon[i] = loadImage(filename);
    
  }

  fill(#FFFFFF);
  rect(410, 280, 200, 100, 28);

  fill(#000000);
  text("Iniciar", 447, 345);
}

void mousePressed() {
  if (mouseX > 410 && mouseX < 610 && mouseY > 280 && mouseY < 380) {
    background(pokedex);
    visivel = 1;
    fill(255, 0, 0);
    rect(635, 340, 125, 40);
    fill(0);
    textSize(20);
    text("Vine Whip", 655, 365);
    fill(255, 0, 0);
    rect(865, 340, 125, 40);
    fill(0);
    textSize(20);
    text("Razor Leaf", 885, 365);
  }

  if ((mouseX>650)&&(mouseX<750)&&(mouseY>350)&&(mouseY<390)) {
    movie = 1;
    i = video; //busca o video da primeira habilidade de cada pokemon, iniciado em 0
  }
  if ((mouseX>850)&&(mouseX<1000)&&(mouseY>350)&&(mouseY<390)) {
    movie = 1;
    i = video + 1; //busca o video da segunda habilidade de cada pokemon, somando +1 para seguir a sequência
  }
  if ((mouseX>=104)&&(mouseY<=55)) {
    minim = new Minim(this);
    song = minim.loadFile("pokedex_pokemon.mp3");
    song.play();
  }
  
  
}

void keyPressed() {
  if (keyCode == RIGHT) { //Lucas - Muda do Pokémon atual para o próximo
    index = (index + 1) % pokemon.length;
    video = (video + 2) % habilidades.length; // Larissa - muda a variavel dos videos de habilidade de cada pokemon
    background(pokedex);
    fill(255, 0, 0);
    rect(635, 340, 125, 40);
    fill(0);
    textSize(20);
    text(habilidade1[index], 700, 360);
    fill(255, 0, 0);
    rect(865, 340, 125, 40);
    fill(0);
    textSize(20);
    text(habilidade2[index], 930, 360);
  }
}

void draw() {
  if (visivel == 1) {
    tela_principal();
  }
  if (movie == 1) { //Larissa - mostra o video da habilidade selecionada quando o botão for acionado
    habilidadesMovies[i].play();
    image(habilidadesMovies[i], 610, 415, 400, 200);
    if (keyPressed) {
      if (keyCode == RIGHT) habilidadesMovies[i].stop(); //Larissa - para o vídeo caso o usuário decida avançar
    }
    if (habilidadesMovies[i].time() == habilidadesMovies[i].duration()) {  //Larissa - remove o vídeo da tela quando ele termina
      movie = 0;
      tela_principal();
  }
  }
  
  if(mouseX > 100   && mouseX < 40 && mouseY > 440 && mouseY < 500) {
    background(pokedex);
    image(charmander, 70,160,130,130);
    image(charmelion, 230, 190,85,85);
    image(charizard,360,180,85,85);
    image(bulbasaur, 110, 270, 60,60);
    image(ivysaur, 220, 270,75,60);
    image(venusaur,365,250,80,80);
    image(squirtle, 110, 330,60,60);
    image(wartortle, 220, 325,95,70);
    image(blastoise, 365,310,80,80);}
  
}



void tela_principal() { //Lucas - informação de cada pokemon e suas posições
  image(pokemon[index], 160, 190, 200, 200);
  textSize(16);
  textAlign(CENTER, CENTER);
  textSize(50);
  text(names[index], 800, 200);
  textSize(20);
  text(types[index], 800, 250);
  text(altura[index], 800, 270);
  text(peso[index], 800, 290);
}


void movieEvent(Movie m) {
  m.read();
}
