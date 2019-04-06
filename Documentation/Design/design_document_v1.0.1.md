<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 5.3.6.1 (Linux)"/>
	<meta name="created" content="00:00:00"/>
	<meta name="changed" content="00:00:00"/>
	<style type="text/css">
		@page { margin-left: 1in; margin-right: 1in; margin-top: 0.39in; margin-bottom: 0.49in }
		@page:first { }
		p { margin-bottom: 0.1in; line-height: 120%; text-align: justify }
		h1 { margin-top: 0in; margin-bottom: 0in; direction: ltr; color: #4a86e8; text-align: center; page-break-inside: avoid; orphans: 2; widows: 2 }
		h1.western { font-family: "Roboto Light", serif; font-size: 20pt; font-weight: normal }
		h1.cjk { font-family: "Roboto Light"; font-size: 20pt; font-weight: normal }
		h1.ctl { font-family: "Roboto Light"; font-size: 20pt; font-weight: normal }
		h2 { margin-top: 0in; margin-bottom: 0in; direction: ltr; text-align: left; page-break-inside: avoid; orphans: 2; widows: 2 }
		h2.western { font-family: "Roboto Light", serif; font-weight: normal }
		h2.cjk { font-family: "Roboto Light"; font-weight: normal }
		h2.ctl { font-family: "Roboto Light"; font-weight: normal }
		h3 { margin-top: 0.22in; margin-bottom: 0.06in; direction: ltr; color: #434343; line-height: 100%; text-align: left; page-break-inside: avoid; orphans: 2; widows: 2 }
		h3.western { font-family: "Roboto Light", serif; font-weight: normal }
		h3.cjk { font-family: "Roboto Light"; font-weight: normal }
		h3.ctl { font-family: "Roboto Light"; font-weight: normal }
		a:link { so-language: zxx }
	</style>
</head>
<body dir="ltr">
<div title="header">
	<p style="margin-bottom: 0.57in; line-height: 115%"><br/>

	</p>
</div>
<p align="left" style="margin-bottom: 0.04in; line-height: 138%"><br/>
<br/>

</p>
<p align="center" style="margin-bottom: 0.04in; line-height: 138%"><font color="#4a86e8"><font face="Roboto Thin, serif"><font size="7" style="font-size: 60pt">Design
Document</font></font></font></p>
<p align="center" style="margin-bottom: 0.22in; line-height: 138%"><font color="#666666"><font face="Roboto Thin, serif"><font size="7" style="font-size: 36pt">Project
RCA</font></font></font></p>
<p style="margin-bottom: 0in; line-height: 115%"><font size="4" style="font-size: 14pt">Project:
Robot Controlling Arm</font></p>
<p style="margin-bottom: 0in; line-height: 115%"><font size="4" style="font-size: 14pt">Written
by: INF2E</font></p>
<p style="margin-bottom: 0in; line-height: 115%"><font size="4" style="font-size: 14pt">Client:
 Mark van der Staaij, <br/>
Bert Meijerink</font></p>
<p style="margin-bottom: 0in; line-height: 115%"><font size="4" style="font-size: 14pt">29
March 2019</font></p>
<p style="margin-bottom: 0in; line-height: 115%"><font size="4" style="font-size: 14pt">Emmen,
Netherlands</font></p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<table width="624" cellpadding="7" cellspacing="0">
	<col width="98">
	<col width="119">
	<col width="365">
	<tr>
		<td colspan="3" width="610" height="14" valign="top" bgcolor="#4a86e8" style="background: #4a86e8" style="border-top: none; border-bottom: none; border-left: none; border-right: 1px dashed #ffffff; padding-top: 0in; padding-bottom: 0in; padding-left: 0in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font color="#ffffff"><font face="Roboto Medium, serif"><font size="3" style="font-size: 12pt">DRAWN
			UP BY INF2E</font></font></font></p>
		</td>
	</tr>
	<tr valign="top">
		<td width="98" bgcolor="#ffffff" style="background: #ffffff" style="border-top: 1.00pt dashed #cccccc; border-bottom: 1.00pt dashed #cccccc; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0.07in; padding-left: 0in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Romandy</font></p>
		</td>
		<td width="119" bgcolor="#ffffff" style="background: #ffffff" style="border-top: 1.00pt dashed #cccccc; border-bottom: 1.00pt dashed #cccccc; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Richardson</font></p>
		</td>
		<td width="365" bgcolor="#ffffff" style="background: #ffffff" style="border-top: 1.00pt dashed #cccccc; border-bottom: 1.00pt dashed #cccccc; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0.07in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">romandy.richardson@student.stenden.com</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td width="98" height="22" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Danylo</font></p>
		</td>
		<td width="119" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0.07in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Znamerovskyi</font></p>
		</td>
		<td width="365" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0.07in; padding-right: 0in">
			<p><font size="3" style="font-size: 12pt">danylo.znamerovskyi@student.stenden.com</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td width="98" height="22" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Joris</font></p>
		</td>
		<td width="119" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0.07in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Rietveld</font></p>
		</td>
		<td width="365" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0.07in; padding-right: 0in">
			<p><font size="3" style="font-size: 12pt">joris.rietveld@student.stenden.com</font></p>
		</td>
	</tr>
	<tr valign="top">
		<td width="98" height="22" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Tarik</font></p>
		</td>
		<td width="119" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0.07in; padding-right: 0.07in">
			<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Arrindell</font></p>
		</td>
		<td width="365" bgcolor="#efefef" style="background: #efefef" style="border-top: 1.00pt dashed #cccccc; border-bottom: none; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0.07in; padding-bottom: 0in; padding-left: 0.07in; padding-right: 0in">
			<p><font size="3" style="font-size: 12pt">tarik.arrindell@student.stenden.com</font></p>
		</td>
	</tr>
</table>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<table width="602" cellpadding="7" cellspacing="0">
	<col width="91">
	<col width="58">
	<col width="124">
	<col width="273">
	<tbody>
		<tr>
			<td colspan="4" width="588" height="18" valign="top" bgcolor="#6d9eeb" style="background: #6d9eeb" style="border-top: none; border-bottom: none; border-left: none; border-right: 1.00pt solid #000001; padding-top: 0in; padding-bottom: 0in; padding-left: 0in; padding-right: 0.07in">
				<p align="center" style="orphans: 0; widows: 0"><font color="#ffffff"><font face="Roboto Medium, serif"><font size="5" style="font-size: 18pt">Revision
				history</font></font></font></p>
			</td>
		</tr>
		<tr valign="top">
			<td width="91" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt"><b>Date</b></font></font></p>
			</td>
			<td width="58" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt"><b>Version</b></font></font></p>
			</td>
			<td width="124" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt"><b>Authors</b></font></font></p>
			</td>
			<td width="273" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt"><b>Change
				Log</b></font></font></p>
			</td>
		</tr>
	</tbody>
	<tbody>
		<tr valign="top">
			<td width="91" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">05/04/2019</font></p>
			</td>
			<td width="58" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt">0.1.0</font></font></p>
			</td>
			<td width="124" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">INF2E</font></p>
			</td>
			<td width="273" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0in">
				<p align="left" style="orphans: 0; widows: 0">The initial version
				of the document.</p>
			</td>
		</tr>
	</tbody>
	<tbody>
		<tr valign="top">
			<td width="91" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">05/04/2019</font></p>
			</td>
			<td width="58" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt">1.0.0</font></font></p>
			</td>
			<td width="124" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">INF2E</font></p>
			</td>
			<td width="273" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0in">
				<p align="left" style="orphans: 0; widows: 0">First draft
				delivered to client.</p>
			</td>
		</tr>
	</tbody>
	<tbody>
		<tr valign="top">
			<td width="91" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: none; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">06/04/2019</font></p>
			</td>
			<td width="58" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font face="Roboto, serif"><font size="3" style="font-size: 12pt">1.0.1</font></font></p>
			</td>
			<td width="124" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: 1.00pt solid #d9d9d9; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0.07in">
				<p align="left" style="orphans: 0; widows: 0"><font size="3" style="font-size: 12pt">Joris
				Rietveld</font></p>
			</td>
			<td width="273" bgcolor="#ffffff" style="background: #ffffff" style="border-top: none; border-bottom: 1.00pt dashed #d9d9d9; border-left: 1.00pt solid #d9d9d9; border-right: none; padding-top: 0in; padding-bottom: 0.07in; padding-left: 0.07in; padding-right: 0in">
				<p align="left" style="orphans: 0; widows: 0">Updated the
				reference list and added the missing UR10 chapter under hardware</p>
			</td>
		</tr>
	</tbody>
</table>
<h1 class="western" align="center"><a name="_7o8lsmvx9q35"></a><br/>

</h1>
<p align="justify" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="justify" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western"><a name="_yvzy6q2lpglb"></a><br/>

</h1>
<h1 class="western" style="page-break-before: always"><a name="_90tc6re1epez"></a>
Table Of Contents</h1>
<div id="Table of Contents1" dir="ltr">
	<p><br/>
<br/>

	</p>
</div>
<p align="left" style="margin-top: 0.14in; margin-bottom: 0.06in; line-height: 100%">
<br/>
<br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western"><a name="_vcf0kls9vkoc"></a><br/>

</h1>
<h1 class="western" align="left" style="page-break-before: always"><a name="_390g3c5qfvms"></a>
System Overview</h1>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">The
entire system consists of the robotic arm and the camera. The robotic
arm must be able to pick up physical dices and then sort them. The
dices are sorted by numbers and the sorting is done with the magnetic
gripper and camera. This can also determine the location of the dices
and is done by the means of a grid. The camera looks at which
positions on the grid a dice is located. These dices will be laid in
a fix position on the grid for the robot arm. This is then passed on
to the robotic arm, so it knows where to pick up the dices. It is
then up to the robotic arm to place the dices in the right in sorted
order on to another fixed position on the grid.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">At this
stage of the project, the dices are always at a fixed location. This
has been agreed to keep the project realistic for this time span,
while at the same time thinking of the future when there are several
locations in a prosecution of this project.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">The
Project team is solely responsible for the camera part of the system.
The Project team must select a suitable camera, hardware, and
software.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">
</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%; page-break-before: always">
<br/>

</p>
<h1 class="western" align="left"><a name="_ixx3qxbfgsmg"></a>Hardware</h1>
<h2 class="western"><a name="_seqjedetdh90"></a>Raspberry Pi</h2>
<p style="margin-bottom: 0in; line-height: 115%">The computer vision
system will be run on a raspberry pi connected to the controller of
the universal robot UR10. The raspberry pi installed on the end of
the arm of the UR10 is a “Raspberry Pi 3 Model B+”. At the time
of writing, this is the latest model of the pi but the software would
probably also work on succeeding models. It could probably also be
ported to work on any of the preceding versions of the pi but much
slower because the OpenCV library which is required by our software
is quite resource intensive.
</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">See appendix 2 for
detailed specifications of the raspberry pi used in this project.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western"><a name="_p3crqvg7bgn9"></a>Camera</h2>
<p style="margin-bottom: 0in; line-height: 115%">At the end of the
UR10, there is a colour camera connected to the pi over USB. For our
project, it wouldn't be necessary to use a colour camera because we
will convert the pictures to grayscale before sending them to OpenCV
for object detection. This setup is for relative object detection It
is unclear at the moment if our system also needs to work with static
object detection. Static means that the camera will be set up at a
fixed position separate of the UR10.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western"><a name="_c9iyx0j39ud8"></a>Universal Robot UR10</h2>
<p style="margin-bottom: 0in; line-height: 115%">The UR10 is the
robot that will be used to manipulate the dices placed on the grid.
It is stationed in a closed off environment inside the room 1.015,
this because it is not allowed for students to be within the ams
reach when its operational. The room is equipped with an infrared
sensor that gets triggered when a person enters while the robot is
activated. If you trigger this safety measure you will have to wait
for about 5 seconds and then push on the green button on the box
placed on the right side of the table to re-enable the robot. On the
left side the UR10 controller is placed that connects to a
touchscreen that is used to configure, program, and control the UR10.
</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">See appendix 3 for
detailed specifications of the universal robot and tool used in this
project.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western"><a name="_ijc69u3wxocy"></a>Router</h2>
<p style="margin-bottom: 0in; line-height: 115%">Inside the closed
off environment of the UR10 there is also a router located, this
router is used to connect the raspberry pi and UR10 controller with
each other over ethernet. It also broadcasts a access point that
enables us to connect to the UR10 controller and raspberry pi mounted
on the arm. The name of the access point is: TODO<!-- Lookup the network name -->
and to communicate to the UR10 controller use the ip address : IP<!-- Lookup the IP of the UR10 controller -->
or IP<!-- Lookup the IP of the raspberry pi --> for the raspberry pi.
</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0.11in; line-height: 108%"><br/>
<br/>

</p>
<h1 class="western" align="left"><a name="_caporjeacqc0"></a>Software</h1>
<h2 class="western" align="left"><a name="_x12pwqikq4z0"></a>OpenCV</h2>
<p style="margin-bottom: 0in; line-height: 115%">For object detection
and object localization we are going use OpenCV, we chose this
library because the previous group research found that it was the
best fit for the project and during our research phase we came to the
same conclusion. OpenCV is an open source library initially developed
by a team at Intel but now lives on supported by a large open source
development community. It includes many modules commonly used in
computer vision applications including object recognition and has
bindings for many programming languages like C, C++, Java, and Python
to name a few.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western" align="left"><a name="_2kbm0miu8oq5"></a>Python 3</h2>
<p style="margin-bottom: 0in; line-height: 115%">We chose to use the
OpenCV python binding to create the part of our application that will
handle the video stream, convert it and then localize the dice on the
grid. We are free to choose either python 2 or 3 but because the
python 3 API is more consistent and recommended by the official
python community we choose to use python 3. For executing our python
code we use CPython because this is the standard python interpreter
and on a raspberry pi we wouldn’t gain much if we would use the JIT
from Pypy.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western" align="left"><a name="_4j9sw04ah892"></a>ROS
	</h2>
<p style="margin-bottom: 0in; line-height: 115%">ROS (Robot Operating
System) is an operating system commonly used in robotic applications.
It has default support for the latest version of OpenCV, Universal
Robots and Kuka (which was the robot included in the initial version
of the project). Ros can be installed on top of most Linux based
systems like Ubuntu, Debian (Raspbian) or redhat. We are going to use
ROS on top of raspbian because this is the default operating system
supported by the raspberry pi community which means it has the best
support on the raspberry pi and most learning resources.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western"><a name="_ec7caa3jw29y"></a>URScript</h2>
<p style="margin-bottom: 0in; line-height: 115%">The universal robot
has its own programming language called UR Script, it's a programing
language that has some resemblance with python but it is a domain
specific. There are 2 ways we can implement our software, we could
write all our code in python and generate the URScript commands there
and send them. Or we could write our code in URScirpt and call the
python code on the raspberry pi over Xmlrpc.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western"><a name="_4f0nbhh9lggd"></a>Xmlrpc</h2>
<p style="margin-bottom: 0in; line-height: 115%">XML RPC is created
to make a universal standard way of calling functions over the
network in an XML format. It has implementations for any major
programming language but if we are going to use it we will use the
python library.</p>
<h2 class="western" align="left"><a name="_66lam0h7xzqt"></a><br/>

</h2>
<h1 class="western" align="left" style="page-break-before: always"><a name="_6scpz365500j"></a>
Functionality
</h1>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">The systems
developed by INF2E contains several functionalities to meet the robot
arms requirements.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Below
describes how the system will be able to use the camera's input to
identify the dice and read the numbers on their faces. Within a fixed
location using a Camera and software(OpenCV). To subsequently pass
this information on to the PLC, on which the correct action is
performed.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western" style="line-height: 100%"><a name="_9yhha0h97px3"></a>
Dice recognition</h2>
<p align="left" style="margin-bottom: 0in; line-height: 115%">For
object detection, the robot's camera will work with OpenCV connected
over USB.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">The
images from the camera would then be converted into grayscale and
then sent to openCV</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">for
object detection.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western" style="line-height: 100%"><a name="_tomwe9jaczze"></a>
Location tracking</h2>
<p align="left" style="margin-bottom: 0in; line-height: 115%">For
location tracking the robot's camera will be used along with the
color recognition along with the &quot;Color Labeler&quot;. To
determine the X and Y position. The center point will be calculated
for each contour of an object. This information (X and Y) will then
be stored in combination with the color in an array. There will be 2
modes available for recognizing color and position;</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Mode 1
- Grid Location and color of multiple individual objects within a
grid will be collected and forwarded to the PLC. The X and Y
coordinates are 2D points that, with the help of calibration at the
future camera location, will have to be converted to 3D coordinates
that are useful for the UR15</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Mode 2
- Fixed point Location and color of 1 object placed at a fixed point
(Center of the camera) will be passed on to the PLC. The X and Y
coordinates are 2D points that, with the help of calibration at the
future camera location, will have to be converted to 3D coordinates
that are useful for the Kuka Robot. (Determining object color with
OpenCV, 2018)</p>
<h2 class="western" style="line-height: 100%"><a name="_apy3ussbxndm"></a>
<br/>

</h2>
<h2 class="western" style="line-height: 100%"><a name="_887fhcodfy0e"></a>
Object manipulation</h2>
<p align="left" style="margin-bottom: 0in; line-height: 115%">In
order for the arm to move the 3D printed di to selected area, the di
will have metal printed inside this will allow the magnetic tip of
the arm to grab the dice. In order for the Arm to move to where the
di is located the location tracking of the camera can be calculated
and calibrated to move off-center with the magnetic tip.</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western" style="line-height: 100%"><a name="_494m2tttoypl"></a>
<br/>

</h2>
<h2 class="western" style="line-height: 100%"><a name="_2q796wyo0zw5"></a>
Sorting of dice</h2>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Using
the information from Object Detection, Parameters will be set that
allows OpenCV to group individual Dice and assign the number shown by
their faces, this will allow numbers to be sorted from largest to
smallest or vice versa. If multiple di landed on the same face the
Robot will prioritize the closest duplicated dice.</p>
<h1 class="western" align="left"><a name="_44nm95g3ia9w"></a><br/>

</h1>
<h1 class="western" align="left" style="page-break-before: always"><a name="_74u8u5unak09"></a>
Code conventions</h1>
<h2 class="western"><a name="_yy5fsh177vzf"></a>Python</h2>
<ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">PEP
	20
	</p>
</ul>
<p align="left" style="margin-left: 0.5in; margin-bottom: 0in; line-height: 115%">
The Zen of Python (<a href="https://www.python.org/dev/peps/pep-0020/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0020/</u></font></a>)</p>
<ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">PEP
	8.0
	</p>
</ul>
<p align="left" style="margin-left: 0.5in; margin-bottom: 0in; line-height: 115%">
Style Guide for Python Code
(<a href="https://www.python.org/dev/peps/pep-0008"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0008</u></font></a>)</p>
<ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">PEP
	257</p>
</ul>
<p align="left" style="margin-left: 0.5in; margin-bottom: 0in; line-height: 115%">
Conventions for Docstring in Python
(<a href="https://www.python.org/dev/peps/pep-0257/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0257/</u></font></a>)</p>
<ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">PEP
	287</p>
</ul>
<p align="left" style="margin-left: 0.5in; margin-bottom: 0in; line-height: 115%">
reStructuredText Docstring Format
(<a href="https://www.python.org/dev/peps/pep-0287/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0287/</u></font></a>)</p>
<ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">PEP
	440
	</p>
</ul>
<p align="left" style="margin-left: 0.5in; margin-bottom: 0in; line-height: 115%">
Version Identification and Dependency Specification
(<a href="https://www.python.org/dev/peps/pep-0440/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0440/</u></font></a>)</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h2 class="western"><a name="_xk6kqi6084rk"></a>BASH</h2>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Google Shell
	Style Guide (<a href="https://google.github.io/styleguide/shell.xml"><font color="#1155cc"><u>https://google.github.io/styleguide/shell.xml</u></font></a>)</p>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western" align="left"><a name="_1mh3gawca21n"></a><br/>

</h1>
<h1 class="western" align="left" style="page-break-before: always"><a name="_90ndfsg0dzuw"></a>
References:</h1>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Universal
Robots. (2018). <i>The URScript Programming Language</i> (Version
3.5.4). Retrieved from
http://me.umn.edu/courses/me5286/robotlab/Resources/scriptManual-3.5.4.pdf</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Universal
Robots (2018) User Manual UR10   (Version 3.5.5) Retrieved from
https://s3-eu-west-1.amazonaws.com/ur-support-site/32464/UR10_User_Manual_en_Global-3.5.5.pdf</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Universal
Robots (2018) PolyScope Manual  (Version 3.5.5) Retrieved from
https://s3-eu-west-1.amazonaws.com/ur-support-site/32522/Software_Manual_en_Global-3.5.5.pdf</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Universal
Robots (2018) Service Manual (Version 3.5.5) Retrieved from
https://s3-eu-west-1.amazonaws.com/ur-support-site/15739/ServiceManual_UR10_en_3.2.1.pdf</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Universal
Robots. (n.d.). Profinet Guide - 20596. Retrieved March 29, 2019,
from
<a href="https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/profinet-guide-20596"><font color="#1155cc"><u>https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/profinet-guide-20596</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Python
Software Foundation (2001)  Style Guide for Python Code (PEP 8)
Retrieved from <a href="https://www.python.org/dev/peps/pep-0008"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0008</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Python
Software Foundation (2004)  The Zen of Python (PEP 20) Retrieved from
<a href="https://www.python.org/dev/peps/pep-0020/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0020/</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Python
Software Foundation (2001) Conventions for Docstring in Python  (PEP
257) Retrieved from <a href="https://www.python.org/dev/peps/pep-0257/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0257/</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Python
Software Foundation (2002) reStructuredText Docstring Format  (PEP
287) Retrieved from <a href="https://www.python.org/dev/peps/pep-0287/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0287/</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Python
Software Foundation (2013) Version Identification and Dependency
Specification (PEP 440 ) Retrieved from
<a href="https://www.python.org/dev/peps/pep-0440/"><font color="#1155cc"><u>https://www.python.org/dev/peps/pep-0440/</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Google
(n.b.) Shell Style Guide (Revision 1.26) Received from
<a href="https://google.github.io/styleguide/shell.xml"><font color="#1155cc"><u>https://google.github.io/styleguide/shell.xml</u></font></a></p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Universal
Robots (2014) Technical specifications UR10 (EN 10/2014) Retrieved
from (https://www.universal-robots.com/media/50880/ur10_bz.pdf)</p>
<p align="left" style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western" style="page-break-before: always"><a name="_oug3fyml6o60"></a>
Appendix 1</h1>
<h3 class="western"><a name="_dyra005v1qa0"></a>The current hardware
configuration of the system.</h3>
<p style="margin-bottom: 0in; line-height: 115%">There is a camera
connected to the arm of the UR 10 (Universal Robot 10). The Camera is
connected over USB to the raspberry pi 3, which is used to run the
computer vision software. The software processes the images using the
OpenCV library to determine the current state of the system and plan
the next commands needed to be sent. When the software knows what
command to send next it creates a UDP packet that will be sent over
an ethernet cable connected to the PLC (Siemens S7 1200). The PLC
then translates the commands to instructions for the UR10 and sends
them over an ethernet cable to the controller of the Universal Robot.</p>
<p style="margin-bottom: 0in; line-height: 115%"><img src="output_html_1631bf7570469dd3.png" name="image1.png" align="bottom" width="571" height="339" border="0"/>
</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western" style="page-break-before: always"><a name="_kc4lsuqcjtro"></a>
Appendix 2</h1>
<h2 class="western"><a name="_n8p3iamgvxa8"></a>Specifications
raspberry pi 3 Model B+</h2>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Broadcom
	BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">1GB LPDDR2
	SDRAM</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">2.4GHz and
	5GHz IEEE 802.11.b/g/n/ac wireless LAN, Bluetooth 4.2, BLE</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Gigabit
	Ethernet over USB 2.0 (maximum throughput of 300 Mbps)</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Extended
	40-pin GPIO header</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Full-size
	HDMI</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">4 USB 2.0
	ports</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">CSI camera
	port for connecting a Raspberry Pi camera</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">DSI display
	port for connecting a Raspberry Pi touchscreen display</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">4-pole stereo
	output and composite video port</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Micro SD port
	for loading your operating system and storing data</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">5V/2.5A DC
	power input</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Power-over-Ethernet
	(PoE) support</p>
</ul>
<h1 class="western"><a name="_eccpt6gmn54d"></a><br/>

</h1>
<h1 class="western" style="page-break-before: always"><a name="_ma4ktas2alx4"></a>
Appendix 3</h1>
<h2 class="western"><a name="_t0s5aj2c9zgt"></a>Specifications
Universal Robot UR10</h2>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">6-axis robot
	arm with a working radius of 1300 mm</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Current
	Software version: 1.8.2.1</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Tool: Machnet</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Tool
	connection: Digital IO 8</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Weight:28.9
	kg</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Payload:10 kg
		</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Reach:1300 mm</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Joint
	ranges:+/- 360°</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Speed:
	</p>
	<ul>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">Base and
		Shoulder: 120°/s.
		</p>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">Elbow, Wrist
		1, Wrist 2, Wrist 3: 180°/s.</p>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">Tool:
		Typical 1 m/s.
		</p>
	</ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Repeatability:
	+/- 0.1 mm / (4 mils)</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Footprint:
	Ø190 mm</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Degrees of
	freedom: 6 rotating joints</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Control box
	size (WxHxD): 475 mm x 423 mm x 268 mm
	</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">I/O ports:
	</p>
	<table width="506" cellpadding="0" cellspacing="0">
		<col width="169">
		<col width="169">
		<col width="169">
		<tr valign="top">
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p><br/>

				</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>Controlbox</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>Tool connection</p>
			</td>
		</tr>
		<tr valign="top">
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>Digital in</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>16</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>2</p>
			</td>
		</tr>
		<tr valign="top">
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>Digital out
				</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>16</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>2</p>
			</td>
		</tr>
		<tr valign="top">
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>Analog in</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>2</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>2</p>
			</td>
		</tr>
		<tr valign="top">
			<td width="169" height="23" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>Analog out</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>2</p>
			</td>
			<td width="169" bgcolor="#ffffff" style="background: #ffffff" style="border: none; padding: 0in">
				<p>-</p>
			</td>
		</tr>
	</table>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">I/O power
	supply:
	</p>
	<ul>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">24 V 2A in
		control box
		</p>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">2 V/24 V 600
		mA in tool</p>
	</ul>
</ul>
<p style="margin-left: 1in; margin-bottom: 0in; line-height: 115%"><br/>

</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Communication:
		</p>
	<ul>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">TCP/IP 100
		Mbit: IEEE 802.3u, 100BASE-TX</p>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">Ethernet
		socket &amp; Modbus TCP</p>
	</ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">IP
	classification: IP54</p>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Collaboration
	operation:</p>
	<ul>
		<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">
		15 Advanced Safety Functions</p>
		<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">
		Tested in accordance with:
		</p>
		<ul>
			<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">
			EN ISO 13849:2008 PL d</p>
			<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">
			EN ISO 10218-1:2011, Clause 5.4.3</p>
		</ul>
	</ul>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Materials:
	Aluminum, ABS plastic, PP plastic</p>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Temperature:
	The robot can work in a temperature range of 0-50°C</p>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Power
	supply:100-240 VAC, 50-60 Hz</p>
	<li/>
<p align="left" style="margin-bottom: 0in; line-height: 115%">Cabling:</p>
	<ul>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">Cable
		between robot and control box (6 m )</p>
		<li/>
<p style="margin-bottom: 0in; line-height: 115%">Cable
		between touchscreen and control box (4.5 m)</p>
	</ul>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<div title="footer">
	<p align="right" style="margin-top: 0.47in; margin-bottom: 0in; line-height: 115%">
	<br/>

	</p>
</div>
</body>
</html>