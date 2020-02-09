import React, { Component } from 'react';
import './Login.css'
import { Link } from 'react-router-dom';
import { Redirect } from 'react-router';

const axios = require('axios');

class Login extends Component {
	constructor(props) {
    	super(props);
    	this.handleIdChange = this.handleIdChange.bind(this);
    	this.handlePasswordChange = this.handlePasswordChange.bind(this);
    	this.state = {
      		_id:'',
      		password:'',
            userInfo:[],
            redirect:0
    	};
	}
	handleIdChange(e){
    	this.setState({_id:e.target.value})
	}
	handlePasswordChange(e){
    	this.setState({password:e.target.value})
	}

	_signIn = async () => {
		const userInfo = await this.signInApi()
		this.setState({userInfo: userInfo})
		if (this.state.userInfo.role==='U'){
            localStorage.setItem('userId',this.state.userInfo.id)
            localStorage.setItem('userName',this.state.userInfo.name)
            this.setState({redirect: 1})
		}else if(this.state.userInfo.role==='A'){
            this.setState({redirect:2})
        }else{
            alert('잘못된 아이디 혹은 비밀번호를 입력하셨습니다.')
        }
    }
    signInApi = () => {
		let data= new FormData();
        data.append('id',this.state._id);
        data.append('password', this.state.password);
    	return axios.post('http://54.180.25.155:8020/users/login', data)
		.then(response => response.data)
		.catch(err => console.log(err))
    }

	render(){
	   const { redirect } = this.state;
        if (redirect===1) {
            return <Redirect to='/test' />;
        }
        if (redirect===2){
            return <Redirect to="/manager_ManageEvent" />
        }
        localStorage.clear()
       return(
        <form className="form-signin">
        <h2 className="form-signin-heading"> 로그인  </h2>
        <label for="inputID" className="sr-only"> ID </label>
        <input type="_id" onChange={this.handleIdChange} id="inputID" className="form-control" placeholder="ID" required autofocus />
        <label for="inputPassword" className="sr-only"> Password</label>
        <input type="password" onChange={this.handlePasswordChange} id="inputPassword" className="form-control" placeholder="Password" required />
        <Link to="/FindIdPw"> 아이디 찾기, 비밀번호 찾기 </Link> 
        <Link to="/Signup"> 회원가입 </Link> 
        <button className="btn btn-lg btn-primary btn-block" onClick={this._signIn} type="button"> 로그인 </button>
        </form> 
	   )

	}
}

export default Login;
