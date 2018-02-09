let base_url = "api/";
let word_url = base_url + "words/";
let question_url = base_url + "qs/";
let answer_url = base_url + "as/";

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
	},
	
	methods: {
		getWord: function () {
			axios.get(word_url).then(response => {
				this.vwords = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},

		postWord: function () {
			if (this.vword) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(word_url, {kelime: this.vword}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +response);
					if(response.status == "201"){
						this.vwords.push({kelime: this.vword});
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
//------------QUESTION--------------------------------------------
		getQuest: function () {
			axios.get(question_url).then(response => {
				this.vquestions = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},

		postQuest: function () {
			if (this.vquestion) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(question_url, {question: this.vquestion}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +JSON.stringify(response));
					if(response.status == "201"){
						this.vquestions.push({question: this.vquestion});
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

		onQSubmit: function (event){
			event.preventDefault();
			this.postQuest();		
		},
		onQReset: function (event){
			event.preventDefault();
			this.vquestion = '';
			this.show = false;
			this.$nextTick(() => { this.show = true });
		},
		//------------ANSWER--------------------------------------------
		getAnsw: function () {
			axios.get(answer_url).then(response => {
				this.vanswers = response.data
			})
			.catch(e => {
				console.log(e);
			})
		},

		postAnsw: function () {
			if (this.vanswer) {
				axios.defaults.xsrfCookieName = 'csrftoken';
				axios.defaults.xsrfHeaderName = 'X-CSRFToken';
				axios.post(answer_url, {answer: this.vanswer}, {
					headers: {
						"content-type": "application/json",
					}
				}).
				then((response) => {
					console.log("RESPONSE:" +JSON.stringify(response));
					if(response.status == "201"){
						this.vanswers.push({answer: this.vanswer});
					}
					this.vanswer = null;
				})
				.catch(function (error) {
					console.log(error);
				});
				
			}else{
				this.verror_answer = "Question is empty!";
			}
		},

		onASubmit: function (event){
			event.preventDefault();
			this.postAnsw();		
		},
		onAReset: function (event){
			event.preventDefault();
			this.vanswer = '';
			this.show = false;
			this.$nextTick(() => { this.show = true });
		},
		onQuAnsSubmit: function (event){
			event.preventDefault();
			this.postQuest();
			this.postAnsw();		
		},
		onQueAnsReset: function (event){
			event.preventDefault();
			this.vquestion = '';
			this.vanswer = '';
			this.show = false;
			this.$nextTick(() => { this.show = true });
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