import React, {Component} from 'react';
import { Redirect } from 'react-router';

const axios = require('axios');

class ApplyForm extends Component {
  constructor(props) {
    super(props);
    this.handleUserName = this.handleUserName.bind(this);
    this.handleUserAge = this.handleUserAge.bind(this);
    this.handleUserPNum = this.handleUserPNum.bind(this);
    this.handelCompanyNum = this.handelCompanyNum.bind(this);
    this.onpetChanged = this.onpetChanged.bind(this)
    this.state = {
      userName: '',
      userAge:'',
      userPNum:'',
      applyPath: '인터넷',
      companyNum :0,
      petExperience: 0,
      petTerm:'없음',
      redirect: 0,
      date: new Date()
    };
  }
  _onChange = date => this.setState({date})

  handleUserName(e){
    this.setState({userName:e.target.value})
  }
  handleUserAge(e){
    this.setState({userAge:e.target.value}) 
  }
  handleUserPNum(e){
    this.setState({userPNum:e.target.value}) 
  }
  handelCompanyNum(e){
    this.setState({companyNum:e.target.value})
  }
  onpetChanged(e){
    this.setState({petExperience: e.currentTarget.value})
  }  

  _handleSubmit(e) {
    e.preventDefault();
    let data = new FormData();
    if (!(this.state.userName) || !(this.state.userAge) || !(this.state.companyNum) || !(this.state.applyPath)) {
      alert("양식을 다시 입력해주세요.1")
    }
    else if((this.state.userPNum).length !== 11){
      alert("핸드폰 번호입력에 '-'를 제거하거나 핸드폰 양식에 맞지 않습니다.")
    }
    else if(!(this.state.petExperience)||!(this.state.petTerm)){
      alert("양식을 다시 입력해주세요.2")
    }else{
    data.append('userName',this.state.userName);
    data.append('userAge', this.state.userAge);
    data.append('userPNum',this.state.userPNum);
    data.append('applyPath',this.state.applyPath);
    data.append('companyNum',this.state.companyNum)
    data.append('petExperience',this.state.petExperience);
    data.append('petTerm',this.state.petTerm);
    let _id = localStorage.getItem('userId')
    let _eid = localStorage.getItem('eid')
    axios.post('http://54.180.25.155:8020/apply/'+_id+'/participant/'+_eid, data)
      .then(function (response) {
           console.log(response);
      }).catch(function (error) {
           console.log(error);
      });
    }
    this.setState({redirect: 1})
    console.log(this.state.redirect)
  }

  render() {
    const { redirect } = this.state;
    if (redirect) {
      return <Redirect to='/test' />;
    }
    return (
    <div className="card">
      <div className = "row">
        <div className="col-md-6">
         <form className="form-horizontal">
            <div className="content">
            <div className="form-group">
              <label className="col-sm-3 control-label">이름</label>
              <div className="col-sm-9">
                <input className="" onChange={this.handleUserName}/> 
              </div>
            </div>
            <div className="form-group">
              <label className="col-sm-3 control-label">나이</label>
              <div className="col-sm-9">
                <input className="" onChange={this.handleUserAge}/> 
              </div>
            </div>
            <div className="form-group">
              <label className="col-sm-3 control-label">전화 번호</label>
              <div className="col-sm-9">
                <input className="" onChange={this.handleUserPNum}/> 
              </div>
            </div>
              <div className="form-group">
                <label className="col-sm-3 control-label">동반자 수</label>
                <div className="col-sm-9">
                   <input className="" onChange={this.handelCompanyNum}/> 
                </div>
              </div>
              <div className="form-group">
                <label className="col-sm-3 control-label">지원 경로</label>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <select value={this.state.applyPath} onChange={(e)=>{this.setState({applyPath: e.target.value})}}>
                  <option value="인터넷">인터넷</option>
                  <option value="에브리 타임">에브리 타임</option>
                  <option value="SNS">SNS</option>
                  <option value="기타">기타</option>
                </select>
              </div>
              <div className="form-group"> 
                <label className="col-sm-3 control-label">반려견 양육 유무  </label>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <input type="radio" name="있음" 
                                    value="1" 
                                    checked={this.state.petExperience === "1"} 
                                    onChange={this.onpetChanged} /> Y &nbsp;&nbsp;&nbsp;&nbsp;
                <input type="radio" name="없음" 
                                    value="0" 
                                    checked={this.state.petExperience === "0"} 
                                    onChange={this.onpetChanged} /> N                    
              </div>
              <div className="form-group">
                <label className="col-sm-3 control-label">반려견 양육 기간  </label>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <select value={this.state.petTerm} onChange={(e)=>{this.setState({petTerm: e.target.value})}}>
                  <option value="없음">없음</option>
                  <option value="3년 미만">3년 미만</option>
                  <option value="3년 이상">3년 이상</option>
                </select>  
              </div>

            </div>
            <div className="footer text-center">
              <button type="submit" className="btn btn-info btn-fill" onClick={(e)=>this._handleSubmit(e)}>Submit</button>
            </div>
          </form>
          </div>
      </div>
    </div>
    )
  }
}
export default ApplyForm;