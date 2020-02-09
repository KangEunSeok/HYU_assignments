import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Redirect } from 'react-router';

const axios = require('axios');

class FindIdPw extends Component {
   constructor(props) {
       super(props);
        this.handleNameChangeforId = this.handleNameChangeforId.bind(this);
        this.handleSsnChangeforId = this.handleSsnChangeforId.bind(this);
        this.handleIdChangeforPw = this.handleIdChangeforPw.bind(this);
        this.handleNameChangeforPw = this.handleNameChangeforPw.bind(this);
        this.handleSsnChangeforPw = this.handleSsnChangeforPw.bind(this);
        this.handlePWQChange = this.handlePWQChange.bind(this);
        this.handlePWAChange = this.handlePWAChange.bind(this);
        
       this.state = {
            nameforId:'',
            ssnforId:'',
            idforPw:'',
            nameforPw:'',
            ssnforPw:'',
            passwordQuestionforPw:'',
            passwordAnswerforPw:''
       };
   }
    handleNameChangeforId(e){
        this.setState({nameforId:e.target.value})
    }
    handleSsnChangeforId(e){
        this.setState({ssnforId:e.target.value})
        this.setState({checkSsn:0})
    }


    handleIdChangeforPw(e){
        this.setState({idforPw:e.target.value})
        this.setState({checkId:0})
    }
    handleNameChangeforPw(e){
        this.setState({nameforPw:e.target.value})
    }
    handleSsnChangeforPw(e){
        this.setState({ssnforPw:e.target.value})
        this.setState({checkSsn:0})
    }
    handlePWQChange(e){
        this.setState({passwordQuestionforPw:e.target.value})
    }
    handlePWAChange(e){
        this.setState({passwordAnswerforPw:e.target.value})
    }


   _FindId = async () => {
        let data= new FormData();
        data.append('name',this.state.nameforId);
        data.append('ssn',this.state.ssnforId);
        axios.post("http://54.180.25.155:8020/users/forgetId",data)
        .then(response => {
            if(response.data !== "")
            alert('아이디는 '+response.data+'입니다.')
            
            else
                alert('아이디가 존재하지 않습니다.')
        })
        .catch(err => console.log(err))    
    }
    _FindPw = async () => {
        let data= new FormData();
        data.append('id',this.state.idforPw);
        data.append('name',this.state.nameforPw);
        data.append('ssn',this.state.ssnforPw);
        data.append('pwQuestion',this.state.passwordQuestionforPw);
        data.append('pwAnswer',this.state.passwordAnswerforPw);
        axios.post("http://54.180.25.155:8020/users/forgetPw",data)
        .then(response => {
            if(response.data !== "")
            alert('비밀번호는 '+response.data+'입니다.')
            else
            alert('아이디가 존재하지 않습니다.')})
        .catch(err => console.log(err))    
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
        <h2 className="form-signup-heading"> 아이디 찾기</h2>
        <label className="col-sm-3 control-label"> 이름 </label>
        <input type="text" onChange={this.handleNameChangeforId} id="inputName" className="form-control" placeholder="이름" required autofocus />
        <label className="col-sm-5 control-label"> 주민번호 </label> 
        <input type="_id" onChange={this.handleSsnChangeforId} id="inputID" className="form-control" placeholder="주민번호" required autofocus />
        <button className="btn btn-lg btn-primary btn-block" onClick={this._FindId} type="button"> 확인 </button>
        </form>


        <form className="form-signin">
        <h2 className="form-signup-heading"> 비밀번호 찾기</h2>
        <label className="col-sm-3 control-label"> 아이디 </label>
        <input type="_id" onChange={this.handleIdChangeforPw} id="inputID" className="form-control" placeholder="아이디" required autofocus />
        <label className="col-sm-3 control-label"> 이름 </label>
        <input type="text" onChange={this.handleNameChangeforPw} id="inputName" className="form-control" placeholder="이름" required autofocus />
        <label className="col-sm-5 control-label"> 주민번호 </label> 
        <input type="_id" onChange={this.handleSsnChangeforPw} id="inputID" className="form-control" placeholder="주민번호" required autofocus />
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
    
        <button className="btn btn-lg btn-primary btn-block" onClick={this._FindPw} type="button"> 확인 </button>
        </form>

        </div>

        )
   }
}

export default FindIdPw;