(this["webpackJsonpload-generator"]=this["webpackJsonpload-generator"]||[]).push([[0],{20:function(e,t,a){e.exports=a(46)},25:function(e,t,a){},44:function(e,t,a){},46:function(e,t,a){"use strict";a.r(t);var s=a(0),n=a.n(s),o=a(18),c=a.n(o),r=(a(25),a(8)),l=a.n(r),u=a(2),i=a(3),m=a(5),p=a(4),d=a(6),h=a(7),v=a.n(h),C=(a(44),a(19));function N(e){var t=e.useCase.name===e.selectedUseCaseName;return n.a.createElement("div",{className:"m-2 col"},n.a.createElement("button",{onClick:function(){return e.callback(e.useCase)},className:"btn col-md p-3",id:"useCaseButton",style:{"background-color":t?"#E05CC1":""}},e.useCase.name))}var f=function(e){function t(){return Object(u.a)(this,t),Object(m.a)(this,Object(p.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return n.a.createElement("div",{id:"resultRenderDiv"},n.a.createElement("pre",null,n.a.createElement("span",null,this.props.serverOutput," ")))}}]),t}(s.Component),b=function(e){function t(e){var a;return Object(u.a)(this,t),(a=Object(m.a)(this,Object(p.a)(t).call(this,e))).setSelectedUseCase=function(e){console.log("Selected Usecase ",e),a.setState({serverOutput:"Please wait..",selectedUseCase:e,selectedUseCaseName:e.name}),a.executeCommand(e)},a.executeCommand=function(e){v.a.get("http://localhost:4000/execute",{params:Object(C.a)({},e,{toolName:a.props.toolName})}).then((function(t){var s=t.data;a.setState({serverOutput:s,selectedUseCase:e})}))},a.state={selectedUseCase:a.props.useCases[0],serverOutput:null,selectedUseCaseName:a.props.useCases[0].name},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this;return n.a.createElement("div",{className:"container",id:"myPocContainer"},n.a.createElement("div",{className:"row"},n.a.createElement("h2",{className:"col text-center",id:"myUsecases"},this.props.toolName," Use Cases")),n.a.createElement("div",{className:"row"},this.props.useCases&&this.props.useCases.map((function(t){return n.a.createElement(N,{key:t.id,useCase:t,callback:e.setSelectedUseCase,selectedUseCaseName:e.state.selectedUseCaseName})}))),n.a.createElement("div",{className:"row",id:"myHorizontalSeprator"},"Usecase Results"),null!=this.state.serverOutput&&n.a.createElement("div",{className:"row"},n.a.createElement(f,{serverOutput:this.state.serverOutput})))}},{key:"componentDidMount",value:function(){this.executeCommand(this.state.selectedUseCase)}}]),t}(s.Component),g=function(e){function t(e){var a;return Object(u.a)(this,t),(a=Object(m.a)(this,Object(p.a)(t).call(this,e))).getToolName=function(){var e,t;return l.a.async((function(s){for(;;)switch(s.prev=s.next){case 0:return s.prev=0,s.next=3,l.a.awrap(v.a.get("http://localhost:4000/toolConfig.json"));case 3:e=s.sent,t=e.data,console.log("ToolName ".concat(t.toolName)),a.setState({toolName:t.toolName}),a.getUsecasesByToolName(),s.next=13;break;case 10:s.prev=10,s.t0=s.catch(0),console.log("error in getToolName",s.t0);case 13:case"end":return s.stop()}}),null,null,[[0,10]])},a.getUsecasesByToolName=function(){var e,t;return l.a.async((function(s){for(;;)switch(s.prev=s.next){case 0:return s.prev=0,s.next=3,l.a.awrap(v.a.get("http://localhost:4000/"+a.state.toolName+"/usecase.json"));case 3:e=s.sent,t=e.data,a.setState({useCases:t.usecases}),console.log("Usecases are  ".concat(t.usecases)),s.next=12;break;case 9:s.prev=9,s.t0=s.catch(0),console.log("Error in getUsecasesByToolName ".concat(s.t0));case 12:case"end":return s.stop()}}),null,null,[[0,9]])},a.state={output:"",useCases:[],toolName:null},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){this.getToolName()}},{key:"render",value:function(){return this.state.useCases.length>0?n.a.createElement(b,{useCases:this.state.useCases,toolName:this.state.toolName}):null}}]),t}(s.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(45);c.a.render(n.a.createElement(g,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[20,1,2]]]);
//# sourceMappingURL=main.91d0b9d8.chunk.js.map