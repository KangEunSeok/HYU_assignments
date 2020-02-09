import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Redirect } from 'react-router';

const axios = require('axios');

class Signup extends Component {
   constructor(props) {
       super(props);
        this.handleNameChange = this.handleNameChange.bind(this);
        this.handleSsnChange = this.handleSsnChange.bind(this);
       this.handleIdChange = this.handleIdChange.bind(this);
       this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handlePassword_AgainChange = this.handlePassword_AgainChange.bind(this);
        this.handlePhonenumberChange = this.handlePhonenumberChange.bind(this);
        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handlePWQChange = this.handlePWQChange.bind(this);
        this.handlePWAChange = this.handlePWAChange.bind(this);
       this.state = {
            name:'',
            ssn:'',
            id:'',
            password:'',
            password_again:'',
            phonenumber:'',
            email:'',
            passwordQuestion:'',
            passwordAnswer:'',
            redirect:0,
            checkId:0,
            checkSsn:0
       };
   }
    handleNameChange(e){
        this.setState({name:e.target.value})
    }
    handleSsnChange(e){
        this.setState({ssn:e.target.value})
        this.setState({checkSsn:0})
    }
   handleIdChange(e){
       this.setState({id:e.target.value})
        this.setState({checkId:0})
   }
   handlePasswordChange(e){
       this.setState({password:e.target.value})
   }
    handlePassword_AgainChange(e){
        this.setState({password_again:e.target.value})
    }
    handlePhonenumberChange(e){
        this.setState({phonenumber:e.target.value})
    }
    handleEmailChange(e){
        this.setState({email:e.target.value})
    }
    handlePWQChange(e){
        this.setState({passwordQuestion:e.target.value})
    }
    handlePWAChange(e){
        this.setState({passwordAnswer:e.target.value})
    }


   _signUp = async () => {
      //const uesrInfo = await this.signUpApi()
      if (this.state.password !== this.state.password_again) //p and p_again not same
        {
            alert('비밀번호가 일치하지 않습니다')            
        }
        // ssn is exist
        else if (this.state.checkSsn === 0) {
            alert('주민번호 중복확인을 해주세요')
        }
        // id is exist
        else if (this.state.checkId === 0){
            alert('아이디 중복확인을 해주세요')
        }
        else if (this.state.checkSsn === 1 && this.state.checkId ==1)
        {
            let data= new FormData();
            data.append('id',this.state.id);
            data.append('password',this.state.password);
            data.append('name',this.state.name);
            data.append('ssn',this.state.ssn);
            data.append('phoneNumber',this.state.phonenumber);
            data.append('email',this.state.email);
            data.append('pwQuestion',this.state.passwordQuestion);
            data.append('pwAnswer',this.state.passwordAnswer);

            axios.post("http://54.180.25.155:8020/users/signup",data)
            .then(response =>{ console.log(response)
                alert('회원가입을 성공하였습니다.')})
            .catch(err => console.log(err))
            this.setState({redirect:1})
        }
        else
        {
            alert('정보를 확인해 주세요')
        }
    }
    _checkSsn = async () => {
        const userInfo = await this.signUpApi_Ssn()
       if (userInfo.data === "")
       {
            this.setState({checkSsn:1});
            console.log(userInfo);
            alert("가입이 가능합니다.");
       }
        else
        {
            this.setState({checkSsn:0});
            alert('이미 가입된 회원입니다.');
            console.log(userInfo);
        }
    }
    _checkId = async () => {
       const userInfo = await this.signUpApi_Id()
       if (userInfo.data === "")
       {
            this.setState({checkId:1});
            console.log(userInfo);
            alert("사용이 가능한 아이디 입니다.");
       }
        else
        {
            this.setState({checkId:0});
            alert('사용불가능한 아이디 입니다.');
            console.log(userInfo);
        }
    }

    signUpApi_Id = () => {
        let url = "http://54.180.25.155:8020/users/"+this.state.id+"/check";
       return axios.get(url)
      .then(response => response)
      .catch(err => console.log(err));
    }

    signUpApi_Ssn = () => {
        let data= new FormData();
        data.append('ssn',this.state.ssn);
        return axios.post('http://54.180.25.155:8020/users/check/ssn',data)
        .then(response => response)
        .catch(err => console.log(err));
    }

    duplicateApi = () => {

    }

   render(){
      const { redirect } = this.state;

        if (redirect) {
            return <Redirect to='/' />;
        }
        return(

        <div className = "card">
        <form className="form-signin">
        <h2 className="form-signup-heading"> 회원가입  </h2>
        <label className="col-sm-3 control-label"> 이름 </label>
        <input type="text" onChange={this.handleNameChange} id="inputName" className="form-control" placeholder="이름" required autofocus />
        <label className="col-sm-3 control-label"> 주민번호 </label> 
        <button className="btn btn-sm " type="button" onClick={this._checkSsn}> 중복확인 </button>
        <input type="_id" onChange={this.handleSsnChange} id="inputID" className="form-control" placeholder="주민번호" required autofocus />
        <label className="col-sm-3 control-label"> 아이디 </label>
        <button className="btn btn-sm " type="button" onClick={this._checkId}> 중복확인 </button>
        <input type="_id" onChange={this.handleIdChange} id="inputID" className="form-control" placeholder="아이디" required autofocus />
        <label className="col-sm-5 control-label"> 비밀번호 </label>
        <input type="password" onChange={this.handlePasswordChange} id="inputID" className="form-control" placeholder="비밀번호" required autofocus />
        <label className="col-sm-5 control-label"> 비밀번호 확인 </label>
        <input type="password" onChange={this.handlePassword_AgainChange} id="inputID" className="form-control" placeholder="비밀번호 확인" required autofocus />
        <label className="col-sm-5 control-label"> 전화번호 </label>
        <input type="_id" onChange={this.handlePhonenumberChange} id="inputID" className="form-control" placeholder="전화번호" required autofocus />
        <label className="col-sm-3 control-label"> 이메일 </label>
        <input type="_id" onChange={this.handleEmailChange} id="inputID" className="form-control" placeholder="이메일" required autofocus />
        <label className="col-sm-5 control-label"> 비밀번호 질문  </label>
        <select  className="selectpicker col-sm-7" onChange={this.handlePWQChange}>
            <option value="" className="label">질문을 선택해 주세요</option>
            <option value="기억에 남는 추억의 장소는?">기억에 남는 추억의 장소는?</option>
            <option value="자신의 인생 좌우명은?">자신의 인생 좌우명은?</option>
            <option value="가장 기억에 남는 선생님 성함은?</">가장 기억에 남는 선생님 성함은?</option>
            <option value="타인이 모르는 신체 비밀이 있다면?">타인이 모르는 신체 비밀이 있다면?</option>
            <option value="받았던 선물 중 기억에 남는 독특한 선물은?">받았던 선물 중 기억에 남는 독특한 선물은?</option>
            <option value="유년시절 가장 생각나는 친구 이름은?">유년시절 가장 생각나는 친구 이름은?</option>
            <option value="인상 깊게 읽은 책 이름은?">인상 깊게 읽은 책 이름은?</option>
            <option value="읽은 책 중에서 좋아하는 구절이 있다면?">읽은 책 중에서 좋아하는 구절이 있다면?</option>
            <option value="자신이 두 번째로 존경하는 인물은?">자신이 두 번째로 존경하는 인물은?</option>
            <option value="친구들에게 공개하지 않은 어릴 적 별명이 있다면?">친구들에게 공개하지 않은 어릴 적 별명이 있다면?</option>
        </select>
       
        <input type="_id" onChange={this.handlePWAChange} id="inputID" className="form-control" placeholder="비밀번호 답" required autofocus />
    
        <button className="btn btn-lg btn-primary btn-block" onClick={this._signUp} type="button"> 확인 </button>
        </form>

        </div>
        )
   }
}

export default Signup;