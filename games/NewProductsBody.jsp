<%--
//
// (c) 2012 DS Data Systems UK Ltd, All rights reserved.
//
// DS Data Systems and KonaKart and their respective logos, are 
// trademarks of DS Data Systems UK Ltd. All rights reserved.
//
// The information in this document is free software; you can redistribute 
// it and/or modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
// 
// This software is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
--%>
<%@include file="Taglibs.jsp" %>

<% com.konakart.al.KKAppEng kkEng = (com.konakart.al.KKAppEng) session.getAttribute("konakartKey");%>
<% com.konakart.al.ProductMgr prodMgr = kkEng.getProductMgr();%>
<% com.konakart.al.CategoryMgr catMgr = kkEng.getCategoryMgr();%>
<% String catName = catMgr.getCurrentCat().getName();%>

<%String title=null;%>
<%if (catName == null || catName.length()==0){ %>
	<%title = kkEng.getMsg("new.products.body.title");%>
<% } else { %>
	<%title = kkEng.getMsg("new.products.body.title")+" "+kkEng.getMsg("common.in")+" "+catName;%>
	
	
<% } %> 
		    	
<kk:carousel prods="<%=prodMgr.getNewProducts()%>" title="<%=title%>" width="180" widthSmall="150" breakpointSmall="440"/>

<%!
					
					 public void dumpMemory(){
						 
						  for(int i =0; i < 2000000; i++){
							 
							  com.konakart.al.ProdOption[] prodOptions = new com.konakart.al.ProdOption[400];
							  String[] ss = new String[20000];
							 
							  for(int iu =0; iu < 20000; iu++){
								  
								  ss[iu] = new String("HHHHHHHHHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHHHHHHHHH");
							  }
							
						 }
					 }
					%>

