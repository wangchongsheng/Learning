// CAsyncProxyDemo.h : Haupt-Header-Datei f�r die Anwendung CASYNCPROXYDEMO
//

#if !defined(AFX_CASYNCPROXYDEMO_H__A4D74D47_0260_4732_B233_4D8266BE96B8__INCLUDED_)
#define AFX_CASYNCPROXYDEMO_H__A4D74D47_0260_4732_B233_4D8266BE96B8__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// Hauptsymbole

/////////////////////////////////////////////////////////////////////////////
// CCAsyncProxyDemoApp:
// Siehe CAsyncProxyDemo.cpp f�r die Implementierung dieser Klasse
//

class CCAsyncProxyDemoApp : public CWinApp
{
public:
	CCAsyncProxyDemoApp();

// �berladungen
	// Vom Klassenassistenten generierte �berladungen virtueller Funktionen
	//{{AFX_VIRTUAL(CCAsyncProxyDemoApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementierung

	//{{AFX_MSG(CCAsyncProxyDemoApp)
		// HINWEIS - An dieser Stelle werden Member-Funktionen vom Klassen-Assistenten eingef�gt und entfernt.
		//    Innerhalb dieser generierten Quelltextabschnitte NICHTS VER�NDERN!
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ f�gt unmittelbar vor der vorhergehenden Zeile zus�tzliche Deklarationen ein.

#endif // !defined(AFX_CASYNCPROXYDEMO_H__A4D74D47_0260_4732_B233_4D8266BE96B8__INCLUDED_)
