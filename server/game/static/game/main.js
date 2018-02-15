let base_url = "api/";
let word_url = base_url + "words/";
let question_url = base_url + "qs/";
let answer_url = base_url + "as/";
let random_word_url = word_url + "0/";
let random_question_url =  question_url + "0/";
let random_answer_url =  answer_url + "0/";
let qw_rel_url = base_url + "qw_rel/";
let aw_rel_url = base_url + "aw_rel/";

var vroot = new Vue({
	delimiters: ['[[', ']]'],
	el: '#root',
	data: {
		vwords: [],
		vquestions: [],
		vanswers: [],
		vword: null,
		vquestion : null,
		vanswer: null,
		verror_word : null,
		verror_question : null,
		verror_answer : null,
		//--------------------------
		show: true,
		game1_display : "inline",
		game2_display : "none",
		game3_display : "none",
		game4_display : "none",
		//--------------------------
		random_word : "",
		random_question: "",
		random_answer: ""
	},
	methods : {
		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ WORD ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/

		/*-------------------------- GET WORD --------------------------*/
		getWord: function () {
			axios.get(word_url).then(response => {
				this.vwords = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},
		/*---------------------------- POST WORD ----------------------------*/
		postWord: function () {
			if (this.vword) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(word_url, {name: this.vword}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +response);
					if(response.status == "201"){
						this.vwords.push({name: this.vword});
					}
					this.vword = null;
				})
				.catch(function (error) {
					console.log(error);
				});
				
			}else{
				this.verror_word = "Input is empty!";
			}
		},
		/*------------------------- GET RANDOM WORD -------------------------*/
		getRandomWord: function () {
			axios.get(random_word_url).then(response => {
				this.random_word = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},


		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ QUESTION ]]]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/

		/*-------------------------- GET QUESTION --------------------------*/
		getQuest: function () {
			axios.get(question_url).then(response => {
				this.vquestions = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},
		/*-------------------------- POST QUESTION --------------------------*/
		postQuest: function () {
			if (this.vquestion) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(question_url, {sentence: this.vquestion}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +JSON.stringify(response));
					if(response.status == "201"){
						this.vquestions.push({sentence: this.vquestion});
					}
					this.vquestion = null;
				})
				.catch(function (error) {
					console.log(error);
				});
				
			}else{
				this.verror_question = "Question is empty!";
			}
		},
		/*------------------------ GET RANDOM QUESTION ------------------------*/
		getRandomQuestion: function () {
			axios.get(random_question_url).then(response => {
				this.random_question = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},

		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ ANSWER ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/

		/*------------------------- GET ANSWER -------------------------*/
		getAnsw: function () {
			axios.get(answer_url).then(response => {
				this.vanswers = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},
		/*------------------------- POST ANSWER -------------------------*/
		postAnsw: function () {
			if (this.vanswer) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(answer_url, {sentence: this.vanswer}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +JSON.stringify(response));
					if(response.status == "201"){
						this.vanswers.push({sentence: this.vanswer});
					}
					this.vanswer = null;
				})
				.catch(function (error) {
					console.log(error);
				});
				
			}else{
				this.verror_answer = "Answer is empty!";
			}
		},
		/*---------------------- GET RANDOM ANSWER ----------------------*/
		getRandomAnswer: function () {
			axios.get(random_answer_url).then(response => {
				this.random_answer_url = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},


		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ QUESTİON WORD REL ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/

		/*------------------------- GET QW REL  -------------------------*/
		getQWrel: function () {
			axios.get(qw_rel_url).then(response => {
				//this.vword.id  = response.data.word
				//this.vquestion = response.data.question
			})
			.catch(e => {
				console.log(e);
			})
		},
		/*------------------------- POST QW REL -------------------------*/
		postQWrel: function () {
			if (this.vanswer) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(qw_rel_url, {
					word: this.random_word.id,
					question: {sentence: this.vquestion}
				}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +JSON.stringify(response));
					if(response.status == "201"){
						this.vquestions.push({sentence: this.vquestion});
					}
					this.vquestion = null;
				})
				.catch(function (error) {
					console.log(error);
				});
				
			}else{
				this.verror_question = "Question is empty!";
			}
		},

		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ ANSWER WORD REL ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/

		/*------------------------- GET AW REL  -------------------------*/
		getAWrel: function () {
			axios.get(aw_rel_url).then(response => {
				//this.vword.id  = response.data.word
				//this.vanswer = response.data.answer
			})
			.catch(e => {
				console.log(e);
			})
		},
		/*------------------------- POST AW REL -------------------------*/
		postAWrel: function () {
			if (this.vanswer) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(aw_rel_url, {
					word: this.random_word.id,
					answer: {sentence: this.vanswer}
				}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +JSON.stringify(response));
					if(response.status == "201"){
						this.vanswers.push({sentence: this.vanswer});
					}
					this.vanswer = null;
				})
				.catch(function (error) {
					console.log(error);
				});
				
			}else{
				this.verror_answer = "Answer is empty!";
			}
		},
		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[ SUBMIT GAMES ]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/
		onGame1Submit: function (event){
			//Important =>  preventDefault!!!, When alert happen dont refreshes
			event.preventDefault();
			if( this.vquestion.toLowerCase().indexOf(this.random_word.name.toLowerCase().slice(0, -1)) == -1 ){
				//Console.log("\n\n\n\n" + this.random_word.slice(0, -1));
				alert("Sorunuz kelimeyi içermiyor!");
			}else if(this.vanswer.indexOf(this.random_word.name.slice(0, -1)) == -1){
				alert("Cevabınız kelimeyi içermiyor!");
			}else{
				this.postQWrel();
				this.postAWrel();
			}			
		},
		onGame1Reset: function (event){
			event.preventDefault();
			this.vquestion = '';
			this.vanswer = '';
			this.show = false;
			this.$nextTick(() => { this.show = true });
		},
		/*-------------------------------------------------------------------*/
		onGame2Submit: function (event){
			//Important =>  preventDefault!!!, When alert happen dont refreshes
			event.preventDefault();
			if( this.vquestion.toLowerCase().indexOf(this.random_word.name.toLowerCase().slice(0, -1)) == -1 ){
				//Console.log("\n\n\n\n" + this.random_word.slice(0, -1));
				alert("Sorunuz kelimeyi içermiyor!");
			}else{
				this.postQWrel();
				this.postAnsw();
			}
		},
		onGame2Reset: function (event){
			event.preventDefault();
			this.vquestion = '';
			this.vanswer = '';
			this.show = false;
			this.$nextTick(() => { this.show = true });
		},
		/*-------------------------------------------------------------------*/
		onGame3Submit: function (event){
			//Important =>  preventDefault!!!, When alert happen dont refreshes
			event.preventDefault();
			if(this.vanswer.toLowerCase().indexOf(this.random_word.name.toLowerCase().slice(0, -1)) == -1){
				alert("Cevabınız kelimeyi içermiyor!");
			}else{
				this.postQuest();
				this.postAWrel();		
			}
		},
		onGame3Reset: function (event){
			event.preventDefault();
			this.vquestion = '';
			this.vanswer = '';
			this.show = false;
			this.$nextTick(() => { this.show = true });
		},

		/*=======================================================================================*/
		/*[[[[[[[[[[[[[[[[[[[[[[[[[[[ CHANGE GAME ]]]]]]]]]]]]]]]]]]]]]]]]]]]*/
		/*=======================================================================================*/
		changeGame: function (){
			//event.preventDefault();
			if(this.game1_display == "inline"){
				this.getRandomWord();
				this.game1_display = "none";
				this.game2_display = "inline";
			}else if(this.game2_display == "inline"){
				this.getRandomWord();
				this.game2_display = "none";
				this.game3_display = "inline";
			}else if(this.game3_display == "inline"){
				this.getRandomQuestion();
				this.game3_display = "none";
				this.game4_display = "inline";

			}else if(this.game4_display == "inline"){
				this.getRandomWord();
				this.game4_display = "none";
				this.game1_display = "inline";
			}else{
				this.game1_display = "none";
				this.game2_display = "none";
				this.game3_display = "none";
				this.game4_display = "none";
			}

		},
	},

	computed: {
		vwords_rev: function () {
			return this.vwords.reverse();
		},
		vquestions_rev: function () {
			return this.vquestions.reverse();
		},
		vanswers_rev: function () {
			return this.vanswers.reverse();
		}
	},

});

vroot.getWord();
vroot.getQuest();
vroot.getAnsw();
vroot.getRandomWord();
//vroot.getRandomQuestion();